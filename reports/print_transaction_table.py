def print_transaction_table(
    transactions,
):
    print()
    print()

    print(
        f"{'ID':<10}"
        f"{'DATE/TIME':<20}"
        f"{'TRANSACTION NAME':<25}"
        f"{'AMOUNT':<14}"
        f"{'CATEGORY':<22}"
        f"{'SUBCATEGORY':<35}"
        f"{'PRIORITY':<10}"
    )

    print("=" * 135)

    for transaction_id, transaction_details in transactions.items():
        transaction_datetime = (
            transaction_details["transaction_datetime"]
        )
        transaction_name = (
            transaction_details["transaction_name"]
        )
        cost = transaction_details["cost"]
        category = transaction_details["category"]
        subcategory = transaction_details["subcategory"]
        priority = transaction_details["priority"]

        print(
            f"{transaction_id:<10}"
            f"{transaction_datetime:<20}"
            f"{transaction_name.title():<25}"
            f"{f'${cost:,.2f}':<14}"
            f"{category.title():<22}"
            f"{subcategory.title():<35}"
            f"{priority.title():<10}"
        )

    print("-" * 135)