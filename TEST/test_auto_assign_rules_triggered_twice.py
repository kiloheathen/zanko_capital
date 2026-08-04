subcategory_assign_rules = {
    "starbucks to coffee shop": {
        "assign_to": "coffee shop",
        "conditions": [
            {
                "field": "transaction_name",
                "operator": "contains",
                "value": "starbucks",
            },
        ],
    },

    "purchases under 10 to snacks": {
        "assign_to": "snacks",
        "conditions": [
            {
                "field": "cost",
                "operator": "less_than",
                "value": 10,
            },
        ],
    },
}