def prompt_user_for_subcategory(
    transactions,
    subcategories,
):
    for transaction_id, transaction_details in transactions.items():
        if not transaction_details["subcategory"]:

            while True:
                print(
                    f"{transaction_details['transaction_name']}: "
                    f"${transaction_details['cost']:.2f}"
                )
                print(transaction_details["transaction_datetime"])
                print("Subcategories:",", ".join(subcategories),)
                print()

                user_defined_subcategory = (
                    input("input subcategory >>> ").lower().strip()
                )

                print()

                subcategory_is_valid = (
                    validate_user_defined_subcategory(
                        user_defined_subcategory,
                        subcategories,
                    )
                )

                if subcategory_is_valid:
                    transaction_details["subcategory"] = (
                        user_defined_subcategory
                    )
                    break

    return transactions


def validate_user_defined_subcategory(
    user_defined_subcategory,
    subcategories,
):
    if user_defined_subcategory in subcategories:
        return True

    print("ERROR: Invalid Subcategory")
    print("Please enter one of the listed subcategories.")
    print()

    return False