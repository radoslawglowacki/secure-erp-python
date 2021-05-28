from model.hr import hr
from view import terminal as view

LIST_OF_LABELS = ["Enter name", "Enter date of birth", "Enter department", "Enter clearance"]
USER_ID_LABEL = "Enter user ID"


def list_employees():
    view.print_table(hr.import_all_employees())


def add_employee():
    inputs = view.get_inputs(LIST_OF_LABELS)
    hr.add_employee(inputs)


def update_employee():
    pass


def delete_employee():
    pass


def get_oldest_and_youngest():
    pass


def get_average_age():
    pass


def next_birthdays():
    pass


def count_employees_with_clearance():
    pass


def count_employees_per_department():
    pass


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
