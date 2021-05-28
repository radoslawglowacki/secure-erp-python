""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def import_all():
    first_place = 0
    to_return = data_manager.read_table_from_file(DATAFILE)
    to_return.insert(first_place, HEADERS)
    return to_return


def add_customer(list_of_inputs):
    new_user = []
    list_of_all_users = data_manager.read_table_from_file(DATAFILE)

    new_user.append(util.generate_id())
    for element in list_of_inputs:
        new_user.append(element)

    list_of_all_users.append(new_user)

    data_manager.write_table_to_file(DATAFILE, list_of_all_users)


def update_customer(list_of_inputs, user_id):
    list_of_all_users = data_manager.read_table_from_file(DATAFILE)
    index_of_id = 0
    for user in list_of_all_users:
        if user_id == user[index_of_id]:
            for i in range(0, len(list_of_inputs)):
                user[i + 1] = list_of_inputs[i]
            data_manager.write_table_to_file(DATAFILE, list_of_all_users)


def remove_user(user_id):
    list_of_all_users = data_manager.read_table_from_file(DATAFILE)
    index_of_id = 0

    for user in list_of_all_users:
        if user[index_of_id] == user_id:
            list_of_all_users.remove(user)
            data_manager.write_table_to_file(DATAFILE, list_of_all_users)


def get_emails_of_subscribed():
    list_of_all_users = data_manager.read_table_from_file(DATAFILE)
    subscription_status_index = 3
    mail_index = 2
    correct_status_of_subscription = "1"
    mails = []

    for user in list_of_all_users:
        if user[subscription_status_index] == correct_status_of_subscription:
            mails.append(user[mail_index])

    return mails
