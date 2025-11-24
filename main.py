from sqlalchemy import create_engine, text
import pandas as pd
import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

class connection:
    # Engine to connect python to SQL
    def create_engine_(self):
        driver_version = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
        if not driver_version:
            raise Exception("SQL Server ODBC driver not found.")
        host = os.getenv('DATABASE_HOST')
        database_name = os.getenv('DATABASE_NAME')
        trusted_connection = "yes"
        connection_string = f"mssql+pyodbc://@{host}/{database_name}?driver={driver_version[0]}&trusted_connection={trusted_connection}"
        return create_engine(connection_string)
    
    # Select on SQL table
    def select_table(self, table, columns='*', condition='1=1'):
        engine = self.create_engine_()
        try:
            query = text(f"SELECT {columns} FROM {table} WHERE {condition}")
            return pd.read_sql(query, engine)
        finally:
            engine.dispose()

    # Insert on SQL TABLE
    def insert_rows(self, table, columns, values):
        """
        columns: ['col1', 'col2']
        values:  [value1, value2]
        """
        engine = self.create_engine_()
        try:
            placeholders = ", ".join([f":{col}" for col in columns])
            colnames     = ", ".join(columns)
            query = text(
                f"INSERT INTO {table} ({colnames}) VALUES ({placeholders})"
            )
            with engine.begin() as conn:
                conn.execute(query, dict(zip(columns, values)))
        finally:
            engine.dispose()

    # Delete from SQL TABLE
    def delete_rows(self, table, condition="1=1"):
        engine = self.create_engine_()
        try:
            query = text(f"DELETE FROM {table} WHERE {condition}")
            with engine.begin() as conn:
                conn.execute(query)
        finally:
            engine.dispose()
    
    # Update SQL TABLE
    def update_rows(self, table, column, value, condition="1=1"):
        engine = self.create_engine_()
        try:
            query = text(
                f"UPDATE {table} SET {column} = :value WHERE {condition}"
            )
            with engine.begin() as conn:
                conn.execute(query, {"value": value})
        finally:
            engine.dispose()

    # Get all the tables linked to the Database
    def get_all_tables(self):
        engine = self.create_engine_()
        try:
            query = text("""
                SELECT TABLE_SCHEMA, TABLE_NAME 
                FROM INFORMATION_SCHEMA.TABLES
            """)
            return pd.read_sql(query, engine)
        finally:
            engine.dispose()

if __name__ == '__main__':
    pass