from sqlalchemy import create_engine, pool, text
from db_manager.settings import get_default_conn_uri
from flask import current_app


class DatabaseManager:
    """
    This class connects to db and fetch/update data based on query passed
    """
    def __init__(self):
        default_conn_pool = create_engine(
            get_default_conn_uri(), poolclass=pool.QueuePool,
            pool_size=current_app.config['POOL_SIZE'], pool_recycle=14400,
            pool_pre_ping=True)
        self.connection = default_conn_pool.connect()

    def fetchall(self, query):
        """
        Return all rows as a dict
        """
        return self.connection.execute(text(query)).mappings().all()

    def create_table(self, create_table_query):
        """
        Create a table in the database if it doesn't exist.
        """
        try:
            self.connection.execute(text(create_table_query))
            self.connection.commit()
        except Exception as e:
            print(f"Error creating table: {e}")

    def insert(self, insert_query):
        """
        Insert data into the table.
        """
        try:
            self.connection.execute(text(insert_query))
            self.connection.commit()
        except Exception as e:
            print(f"Error inserting data into the table: {e}")

    def create_extension(self, query):
        """
        Create Extension for UUID-OSSP
        """
        self.connection.execute(text(query))

    def drop_table(self, drop_table_query):
        """
        Drop the table.
        """
        try:
            self.connection.execute(text(drop_table_query))
            self.connection.commit()
        except Exception as e:
            print(f"Error in drop data: {e}")

    def close_connection(self):
        """
        Close connection
        """
        try:
            self.connection.close()
        except Exception as e:
            print(f"Error in close connection: {e}")

