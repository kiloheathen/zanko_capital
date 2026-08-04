def print_transaction_pivot(
    transactions,
):
    transaction_pivot = prepare_pivot_table(transactions,)

    print()
    print("=" * 68)
    print(f'|{"SPENDING BREAKDOWN":^66}|')
    print("=" * 68)

    print()
    print(
        f'{"PRIORITY > CATEGORY > SUBCATEGORY":<52}'
        f'{"AMOUNT":>13}'
    )
    print("=" * 70)

    priorities = transaction_pivot["priorities"]

    for priority, priority_details in priorities.items():
        print()

        priority_cost = priority_details["total"]

        print(
            f"{priority.title():<52}"
            f"${priority_cost:>12,.2f}"
        )

        categories = priority_details["categories"]

        for category, category_details in categories.items():
            print()

            category_cost = category_details["total"]

            print(
                f"  {category.title():<50}"
                f"${category_cost:>12,.2f}"
            )

            subcategories = category_details["subcategories"]

            for subcategory, subcategory_cost in subcategories.items():
                print(
                    f"    {subcategory.title():<48}"
                    f"${subcategory_cost:>12,.2f}"
                )

        print()
        print("-" * 70)

    grand_total = transaction_pivot["total"]

    print(
        f'{"GRAND TOTAL":<52}'
        f'${grand_total:>12,.2f}'
    )


def prepare_pivot_table(
    transactions,
):
    transaction_pivot = {
        "total": 0,
        "priorities": {},
    }

    for transaction_details in transactions.values():
        priority = transaction_details["priority"]
        category = transaction_details["category"]
        subcategory = transaction_details["subcategory"]

        cost = transaction_details["cost"]
        transaction_pivot["total"] += cost

        if priority not in transaction_pivot["priorities"]:
            transaction_pivot["priorities"][priority] = {
                "total": 0,
                "categories": {},
            }

        transaction_pivot["priorities"][priority]["total"] += cost

        if (category
            not in transaction_pivot["priorities"][priority]["categories"]
        ):
            transaction_pivot["priorities"][priority]["categories"][category] = {
                "total": 0,
                "subcategories": {},
            }

        transaction_pivot["priorities"][priority]["categories"][category][
            "total"
        ] += cost

        if (subcategory
            not in transaction_pivot["priorities"][priority]["categories"][
                category]["subcategories"]
        ):
            transaction_pivot["priorities"][priority]["categories"][category][
                "subcategories"][subcategory] = 0

        transaction_pivot["priorities"][priority]["categories"][category][
            "subcategories"][subcategory] += cost

    return transaction_pivot