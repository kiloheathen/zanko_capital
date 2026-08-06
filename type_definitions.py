from typing import TypedDict


class Conditions(TypedDict):
    field: str
    operator: str
    value: str


# RuleValue: TypeAlias = str | int | float | bool | None
#
# ComparisonOperator: TypeAlias = Literal[
#     "contains",
#     "equals",
#     "less_than",
#     "less_than_or_equal",
#     "greater_than",
#     "greater_than_or_equal",
# ]
#
#
# class RuleCondition(TypedDict):
#     field: str
#     operator: ComparisonOperator
#     value: RuleValue
#
#
# class AssignmentRule(TypedDict):
#     assign_to: str
#     conditions: list[RuleCondition]
#
#
# AssignmentRules: TypeAlias = dict[str, AssignmentRule]