import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection to SQLite DB successful')
    except Error as e:
        print(f'The error "{e}" occured')

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f'The error "{e}" occured')


c = create_connection('D:\\Programs\\pythonProject\\Лекции Колледжа\\test_sqlite3.sql')

create_str = '''
CREATE TABLE IF NOT EXISTS users 
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
nationality TEXT
);
'''
execute_query(c, create_str)
