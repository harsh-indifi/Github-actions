import pandas as pd

from sqlalchemy import text
from extensions import db


class DatabaseManager:
    """
    This class connects to db and fetch/update data based on query passed
    """

    def __init__(self, db_name='default'):
        if db_name == 'bank_statement':
            self.connection = db.engines['bank_statement_db'].connect()
        else:
            self.connection = db.engine.connect()

    def fetchall(self, query):
        """
        Return all rows as a dict
        """
        return self.connection.execute(text(query)).mappings().all()

    def fetch_as_df(self, query):
        """
        Return all rows as a pandas data frame
        """
        return pd.read_sql_query(query, con=self.connection)

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
        Close connection (SQLAlchemy: returns connection to pool for re-using)
        """
        self.connection.close()
