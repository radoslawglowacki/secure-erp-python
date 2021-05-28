""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import CRUD

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def import_all_users():
    first_place = 0
    users_list = CRUD.import_all_records(DATAFILE)
    users_list.insert(first_place, HEADERS)
    return users_list


def add_customer(list_of_inputs):
    CRUD.add_one_record(list_of_inputs, DATAFILE)


def update_customer(list_of_inputs, user_id):
    CRUD.update_record(list_of_inputs, user_id, DATAFILE)


def remove_user(user_id):
    CRUD.remove_record(user_id, DATAFILE)


def get_emails_of_subscribed():
    list_of_all_users = CRUD.import_all_records(DATAFILE)
    subscription_status_index = 3
    mail_index = 2
    correct_status_of_subscription = "1"
    mails = []

    for user in list_of_all_users:
        if user[subscription_status_index] == correct_status_of_subscription:
            mails.append(user[mail_index])

    return mails
