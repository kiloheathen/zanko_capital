subcategory_assign_rules = {
    "starbucks to coffee shop": {
        "assign_to": "coffee shop",
        "conditions": [
            {
                "field": "transaction_name",
                "operator": "contains",
                "value": "starbucks",
            }
        ],
    },

    "starbucks to coffee shop (duplicate rule)": {
        "assign_to": "coffee shop",
        "conditions": [
            {
                "field": "transaction_name",
                "operator": "contains",
                "value": "starbucks",
            }
        ],
    },

    "sheetz under 20 to snacks": {
        "assign_to": "snacks",
        "conditions": [
            {
                "field": "transaction_name",
                "operator": "contains",
                "value": "sheetz",
            },
            {
                "field": "cost",
                "operator": "less_than",
                "value": 15,
            },
        ],
    },

    "sheetz 20 or more to gas": {
        "assign_to": "gas",
        "conditions": [
            {
                "field": "transaction_name",
                "operator": "contains",
                "value": "sheetz",
            },
            {
                "field": "cost",
                "operator": "greater_than_or_equal",
                "value": 15,
            },
        ],
    },

    "netflix to streaming content and subscriptions": {
        "assign_to": "streaming content & subscriptions",
        "conditions": [
            {
                "field": "transaction_name",
                "operator": "contains",
                "value": "netflix",
            }
        ],
    },

    "amc theatres to streaming content and subscriptions": {
        "assign_to": "streaming content & subscriptions",
        "conditions": [
            {
                "field": "transaction_name",
                "operator": "contains",
                "value": "amc theatres",
            }
        ],
    },

    "mortgage transactions to mortgage": {
        "assign_to": "mortgage",
        "conditions": [
            {
                "field": "transaction_name",
                "operator": "contains",
                "value": "mortgage",
            }
        ],
    },

    "electric company transactions to utilities": {
        "assign_to": "utilities",
        "conditions": [
            {
                "field": "transaction_name",
                "operator": "contains",
                "value": "electric company",
            }
        ],
    },
}