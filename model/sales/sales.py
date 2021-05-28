""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import CRUD
import datetime

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def import_all_transaction():
    first_place = 0
    transaction_list = CRUD.import_all_records(DATAFILE)
    transaction_list.insert(first_place, HEADERS)
    return transaction_list


def add_transaction(list_of_inputs):
    CRUD.add_one_record(list_of_inputs, DATAFILE)


def update_transaction(list_of_inputs, transaction_id):
    CRUD.update_record(list_of_inputs, transaction_id, DATAFILE)


def remove_transaction(transaction_id):
    CRUD.remove_record(transaction_id, DATAFILE)


def get_biggest_revenue_transaction():
    transaction_list = CRUD.import_all_records(DATAFILE)
    transaction_revenue_index = 3
    revenues = []

    for transaction in transaction_list:
        revenues.append(float(transaction[transaction_revenue_index]))

    return max(revenues)


def get_biggest_revenue_product():
    transaction_list = CRUD.import_all_records(DATAFILE)
    product_index = 2
    transaction_revenue_index = 3
    products_revenue = {}

    for transaction in transaction_list:
        if transaction[product_index] not in products_revenue:
            products_revenue[transaction[product_index]] = float(transaction[transaction_revenue_index])
        else:
            products_revenue[transaction[product_index]] += float(transaction[transaction_revenue_index])

    ordered_revenues = list(sorted(products_revenue.items(), key=lambda item: item[1], reverse=True))

    return ordered_revenues[0][0]


def get_transaction_between_dates(start, end):
    transaction_list = CRUD.import_all_records(DATAFILE)
    proper_transactions = []
    date_format = '%Y-%m-%d'
    start = datetime.datetime.strptime(start, date_format)
    end = datetime.datetime.strptime(end, date_format)
    transaction_date_index = 4

    for transaction in transaction_list:
        transaction_date = datetime.datetime.strptime(transaction[transaction_date_index], date_format)
        if start <= transaction_date <= end:
            proper_transactions.append(transaction)

    return proper_transactions


def count_transaction_between(start_date, end_date):
    return len(get_transaction_between_dates(start_date, end_date))


def sum_transactions_revenue_between(start_date, end_date):
    transactions_between_dates = get_transaction_between_dates(start_date, end_date)
    index_of_product_price = 3
    sum_of_transactions = 0.0

    for transaction in transactions_between_dates:
        sum_of_transactions += float(transaction[index_of_product_price])

    return sum_of_transactions
