from model.sales import sales
from view import terminal as view

LIST_OF_LABELS = ["Enter product name", "Enter price", "Enter date"]
TRANSACTION_LABEL = "Enter transaction ID"


def list_transactions():
    view.print_table(sales.import_all_transaction())


def add_transaction():
    inputs = view.get_inputs(LIST_OF_LABELS)
    sales.add_transaction(inputs)


def update_transaction():
    transaction_id = view.get_input(TRANSACTION_LABEL)
    inputs = view.get_inputs(LIST_OF_LABELS)
    sales.update_transaction(inputs, transaction_id)


def delete_transaction():
    transaction_id = view.get_input(TRANSACTION_LABEL)
    sales.remove_transaction(transaction_id)


def get_biggest_revenue_transaction():
    view.print_general_results(sales.get_biggest_revenue_transaction(), "Biggest revenue transaction")


def get_biggest_revenue_product():
    view.print_general_results(sales.get_biggest_revenue_product(), "Biggest revenue product")


def count_transactions_between():
    start_date = view.get_input("Enter start date")
    end_date = view.get_input("Enter end date")

    count_transactions = sales.count_transaction_between(start_date, end_date)
    view.print_general_results(count_transactions, "Count transactions between dates")


def sum_transactions_between():
    start_date = view.get_input("Enter start date")
    end_date = view.get_input("Enter end date")

    sum_of_transactions = sales.sum_transactions_revenue_between(start_date,end_date)
    view.print_general_results(sum_of_transactions, "Sum of transactions revenue")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
