from pprint import pprint

import data.load_data
import data.transaction_data
import data.auto_assign_rules
import data.subcategory_definitions

import classification.rule_based_assignment
import classification.lookup_assignment
import classification.manual_assignment

import reports.print_transaction_pivot
import reports.print_transaction_table

transactions = data.load_data.load_raw_transactions(
    data.transaction_data.raw_transactions
)

transactions = data.load_data.add_transaction_fields(
    transactions
)

transactions = classification.rule_based_assignment.auto_assign_subcategories(
    transactions,
    data.auto_assign_rules.subcategory_assign_rules,
)

transactions = classification.manual_assignment.prompt_user_for_subcategory(
    transactions,
    data.subcategory_definitions.subcategories,
)

transactions = classification.lookup_assignment.apply_lookup_assignments(
    transactions,
    data.subcategory_definitions.subcategories,
)

reports.print_transaction_pivot.print_transaction_pivot(
    transactions
)

reports.print_transaction_table.print_transaction_table(
    transactions
)