import psycopg2
from psycopg2 import OperationalError


def create_connection(db, user, password, host, port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print('Connection to PostgreSQL DB successful')
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

