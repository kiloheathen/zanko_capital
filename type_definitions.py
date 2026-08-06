from typing import TypedDict


class Transaction(TypedDict):
    transaction_name: str
    transaction_datetime: str
    cost: float
    category: str | None
    subcategory: str | None
    priority: str | None


Transactions = dict[str, Transaction]


class SubcategoryDefinition(TypedDict):
    category: str
    priority: str


SubcategoryDefinitions = dict[str, SubcategoryDefinition]


class RuleCondition(TypedDict):
    field: str
    operator: str
    value: str | float


class AssignmentRule(TypedDict):
    assign_to: str
    conditions: list[RuleCondition]


AssignmentRules = dict[str, AssignmentRule]