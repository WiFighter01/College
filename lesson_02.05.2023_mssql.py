import pyodbc
from pyodbc import OperationalError


def create_connection(host, user, passwd, db):
    connection = None
    try:
        connection = pyodbc.connect(
            'Driver = ODBC Driver 17 for SQL Server);'
            'Server = "DMITRYPC\SQLEXPRESS";'
            'Database = '+db+';'
            'Trusted_connection=yes;'
        )
        print('Connection to MSSQL DB successful')
    except OperationalError as e:
        print(f'The error "{e}" occured')

    return connection


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except OperationalError as e:
        print(f'The error "{e}" occured')


c = create_connection('DMITRYPC\SQLEXPRESS', 'DMITRYPC', '1234', 'Bel_post_2',)
execute_query(c, 'CREATE DATABASE simple')


'DMITRYPC\SQLEXPRESS'