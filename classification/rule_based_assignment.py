def auto_assign_subcategories(
    transactions,
    subcategory_assign_rules,
):
    for transaction_id, transaction_details in transactions.items():

        matching_rules = evaluate_rules(
            transaction_details,
            subcategory_assign_rules,
        )

        if not matching_rules:
            continue

        if len(matching_rules) == 1:
            selected_rule_name = matching_rules[0]

        else:
            selected_rule_name = prompt_user_for_matching_rule(
                transaction_id,
                transaction_details,
                matching_rules,
                subcategory_assign_rules,
            )

        selected_subcategory = (
            subcategory_assign_rules[selected_rule_name]["assign_to"]
        )

        transaction_details["subcategory"] = selected_subcategory

    return transactions


def evaluate_rules(
    transaction_details,
    subcategory_assign_rules,
):
    matching_rules = []

    for rule_name, rule in subcategory_assign_rules.items():
        rule_matches = True

        for condition in rule["conditions"]:
            field_name = condition["field"]
            actual_value = transaction_details[field_name]
            comparison_operator = condition["operator"]
            comparison_value = condition["value"]

            condition_matches = evaluate_condition(
                actual_value,
                comparison_operator,
                comparison_value,
            )

            if not condition_matches:
                rule_matches = False
                break

        if rule_matches:
            matching_rules.append(rule_name)

    return matching_rules


def evaluate_condition(
    actual_value,
    comparison_operator,
    comparison_value,
):
    if comparison_operator == "contains":
        return comparison_value in actual_value

    if comparison_operator == "equals":
        return actual_value == comparison_value

    if comparison_operator == "less_than":
        return actual_value < comparison_value

    if comparison_operator == "less_than_or_equal":
        return actual_value <= comparison_value

    if comparison_operator == "greater_than":
        return actual_value > comparison_value

    if comparison_operator == "greater_than_or_equal":
        return actual_value >= comparison_value

    return False


def prompt_user_for_matching_rule(
    transaction_id,
    transaction_details,
    matching_rules,
    subcategory_assign_rules,
):
    while True:
        print_transaction_details_for_matching_rules(
            transaction_id,
            transaction_details
        )

        print_rules_to_choose_from(
            matching_rules,
            subcategory_assign_rules,
        )

        user_choice = input("input rule number >>> ").strip()

        print()

        try:
            selected_option = int(user_choice)
        except ValueError:
            print("ERROR: Rule selection must be a whole number.")
            print()
            continue

        if selected_option < 1 or selected_option > len(matching_rules):
            print(
                f"ERROR: Enter a number from 1 "
                f"to {len(matching_rules)}."
            )
            print()
            continue

        selected_index = selected_option - 1

        return matching_rules[selected_index]


def print_transaction_details_for_matching_rules(
        transaction_id,
        transaction_details,
):
    print()
    print("MULTIPLE AUTO-ASSIGN RULES MATCHED")
    print(f"Transaction ID: {transaction_id}")
    print(
        f"{transaction_details['transaction_name']}: "
        f"${transaction_details['cost']:.2f}"
    )
    print(transaction_details["transaction_datetime"])
    print()
    print("Choose which auto-assign rule should be applied:")


def print_rules_to_choose_from(
    matching_rules,
    subcategory_assign_rules,
):
    for option_number, rule_name in enumerate(
            matching_rules,
            start=1,
    ):
        subcategory = (
            subcategory_assign_rules[rule_name]["assign_to"]
        )

        print(
            f"{option_number}. "
            f"{rule_name} -> {subcategory}"
        )

    print()