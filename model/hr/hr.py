""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import CRUD
import datetime
from dateutil.relativedelta import relativedelta

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
DATE_FORMAT = '%Y-%m-%d'


def import_all_employees():
    first_place = 0
    employees_list = CRUD.import_all_records(DATAFILE)
    employees_list.insert(first_place, HEADERS)
    return employees_list


def add_employee(list_of_inputs):
    CRUD.add_one_record(list_of_inputs, DATAFILE)


def update_employee(list_of_inputs, employee_id):
    CRUD.update_record(list_of_inputs, employee_id, DATAFILE)


def remove_employee(employee_id):
    CRUD.remove_record(employee_id, DATAFILE)


def get_oldest_and_youngest():
    employees = CRUD.import_all_records(DATAFILE)
    name_index = 1
    date_index = 2
    dates = {}

    for employee in employees:
        dates[employee[date_index]] = employee[name_index]

    ordered_dates = list(sorted(dates.items(), reverse=True))

    youngest_index = 0
    oldest_index = -1

    return {ordered_dates[youngest_index][1]: ordered_dates[youngest_index][0],
            ordered_dates[oldest_index][1]: ordered_dates[oldest_index][0]}


def average_age():
    employees = CRUD.import_all_records(DATAFILE)
    ages = []
    index_of_employee_birthday = 2

    for employee in employees:
        employee_birthday = datetime.datetime.strptime(employee[index_of_employee_birthday], DATE_FORMAT)
        delta = relativedelta(datetime.datetime.now(), employee_birthday)
        ages.append(delta.years)

    return sum(ages) / len(ages)


def next_birthdays(date):
    employees = CRUD.import_all_records(DATAFILE)
    employees_with_birthdays_names = []
    start = datetime.datetime.strptime(date, DATE_FORMAT)
    end = start + datetime.timedelta(days=14)
    index_of_employee_name = 1
    index_of_employee_birthday = 2

    for employee in employees:
        employee_birthday = datetime.datetime.strptime(employee[index_of_employee_birthday], DATE_FORMAT)
        if start <= employee_birthday <= end:
            employees_with_birthdays_names.append(employee[index_of_employee_name])

    return employees_with_birthdays_names


def count_employees_with_at_least_clearance_lvl(clearance_lvl):
    employees = CRUD.import_all_records(DATAFILE)
    clearance_lvl = int(clearance_lvl)
    proper_employees = []
    clearance_lvl_index = 4

    for employee in employees:
        if int(employee[clearance_lvl_index]) >= clearance_lvl:
            proper_employees.append(employee)

    return len(proper_employees)


def count_employees_by_department():
    employees = CRUD.import_all_records(DATAFILE)
    departments = {}
    department_index = 3

    for employee in employees:
        employee_department = employee[department_index]
        if employee_department not in departments:
            departments[employee_department] = 1
        else:
            departments[employee_department] += 1

    return departments

