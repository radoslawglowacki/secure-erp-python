from model.crm import crm
from view import terminal as view

LIST_OF_LABELS = ["Enter name", "Enter mail", "Enter subscription(1-yes, 0-no)"]
USER_ID_LABEL = "Enter user ID"


def list_customers():
    view.print_table(crm.import_all_users())


def add_customer():
    inputs = view.get_inputs(LIST_OF_LABELS)
    crm.add_customer(inputs)


def update_customer():
    id_of_user = view.get_input(USER_ID_LABEL)
    inputs = view.get_inputs(LIST_OF_LABELS)
    crm.update_customer(inputs, id_of_user)


def delete_customer():
    id_of_user = view.get_input(USER_ID_LABEL)
    crm.remove_user(id_of_user)


def get_subscribed_emails():
    view.print_general_results(crm.get_emails_of_subscribed(), "Emails")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
