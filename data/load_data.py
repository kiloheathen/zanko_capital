def load_raw_transactions(raw_transactions):
    transactions = {}

    for (
        transaction_id,
        transaction_datetime,
        transaction_name,
        cost,
    ) in raw_transactions:
        transactions[transaction_id.strip().lower()] = {
            "transaction_name": transaction_name.strip().lower(),
            "transaction_datetime": transaction_datetime.strip(),
            "cost": float(cost),
            "category": None,
            "subcategory": None,
            "priority": None,
        }

    return transactions