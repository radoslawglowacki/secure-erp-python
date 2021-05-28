from texttable import Texttable


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    for i in range(len(list_options)):
        print("(" + str(i) + ") " + list_options[i])


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    type_of_result = type(result)
    result_string = label + ": "

    if type_of_result == list:
        result_string += "\n"
        for _ in result:
            result_string += str(_) + ", "
    elif type_of_result == dict:
        for k, v in result.items():
            result_string += "\n"
            result_string += str(k) + ": "
            result_string += str(v)
    elif type_of_result == int:
        result_string += str(result)
    elif type_of_result == float:
        result_string += str(round(result, 2))
    elif type_of_result == str:
        result_string += result

    print(result_string)


def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    t = Texttable()
    for i in range(len(table)):
        t.add_row(table[i])
    print(t.draw())


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(label + " : ")


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    inputs = []

    for i in range(0, len(labels)):
        inputs.append(input(labels[i] + " : "))

    return inputs


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print("Error: " + message)
