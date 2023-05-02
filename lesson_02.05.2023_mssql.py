import pyodbc
from pyodbc import Error


def create_connection(host, user, passwd, db):
    connection = None
    try:
        connection = pyodbc.connect(
            'Driver = (SQL Server Native Client 11.0);'
            'Server = '+server+';'
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


c = create_connection('postgres', 'postgres', '1234', '127.0.0.1', '5432')
execute_query(c, 'CREATE DATABASE simple')


'DMITRYPC\SQLEXPRESS'