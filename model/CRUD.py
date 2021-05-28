from model import data_manager, util


def import_all_records(datafile):
    to_return = data_manager.read_table_from_file(datafile)
    return to_return


def add_one_record(list_of_inputs, datafile):
    new_record = []
    list_of_all_records = import_all_records(datafile)

    new_record.append(util.generate_id())
    for _ in list_of_inputs:
        new_record.append(_)

    list_of_all_records.append(new_record)

    data_manager.write_table_to_file(datafile, list_of_all_records)


def update_record(list_of_inputs, record_id, datafile):
    list_of_all_records = import_all_records(datafile)
    index_of_id = 0
    for record in list_of_all_records:
        if record_id == record[index_of_id]:
            for i in range(0, len(list_of_inputs)):
                record[i + 1] = list_of_inputs[i]
            data_manager.write_table_to_file(datafile, list_of_all_records)


def remove_record(record_id, datafile):
    list_of_all_users = import_all_records(datafile)
    index_of_id = 0

    for user in list_of_all_users:
        if user[index_of_id] == record_id:
            list_of_all_users.remove(user)
            data_manager.write_table_to_file(datafile, list_of_all_users)
