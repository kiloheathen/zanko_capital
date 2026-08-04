def apply_lookup_assignments(
    transactions,
    subcategories,
):
    for transaction_details in transactions.values():
        subcategory = transaction_details["subcategory"]

        if not subcategory:
            continue

        lookup_values = subcategories[subcategory]

        for field_name, field_value in lookup_values.items():
            transaction_details[field_name] = field_value

    return transactions