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
        }

    return transactions

def add_transaction_fields(transactions):
    for transaction_details in transactions.values():
        transaction_details["category"] = None
        transaction_details["subcategory"] = None
        transaction_details["priority"] = None

    return transactions