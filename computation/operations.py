import json
from db_manager.database import DatabaseManager
from db_manager.query_manager.query import CREATE_EXTENSION_UUID, CREATE_TABLE_QUERY, \
    INSERT_INTO_TABLE_QUERY, DROP_TABLE_QUERY


class Operations:

    def __init__(self):
        self.db_manager = DatabaseManager()

    def create_extension(self):
        query = CREATE_EXTENSION_UUID
        self.db_manager.create_extension(query)

    def create_table(self, application_table, application_table_columns):
        column_definitions = ", ".join(application_table_columns)
        query = CREATE_TABLE_QUERY.format(application_table, column_definitions)
        self.db_manager.create_table(query)

    def insert_into_table(self, table_name, data_list):
        for data in data_list:
            column_names = ', '.join(f'"{key}"' for key in data.keys())
            values = ', '.join(f"'{value}'" if not isinstance(value, dict) else
                               f"'{json.dumps(value)}'" for value in data.values())
            insert_query = INSERT_INTO_TABLE_QUERY.format(table_name, column_names,
                                                          values)
            self.db_manager.insert(insert_query)

    def fetch(self):
        query = 'Select * from applications'
        return self.db_manager.fetchall(query)

    def drop_table(self, table_name):
        query = DROP_TABLE_QUERY.format(table_name)
        self.db_manager.drop_table(query)

    def close_connection(self):
        self.db_manager.close_connection()


