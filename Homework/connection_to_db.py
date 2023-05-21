import psycopg2
from psycopg2 import Error, OperationalError, ProgrammingError


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
        print('Успешное подключение к базе данных Белпочты')
    except OperationalError as e:
        print(f'The error "{e}" occurred')

    return connection


def execute_query(connection, query):
    '''
    Функция исполняет запрос в базе данных и в случае успешного выполнения выводит
    сообщение об успешном действии
    '''
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Ваш запрос выполнен')
    except OperationalError as e:
        print(f'The error "{e}" occurred')


def fetchall_query(connection, query):
    '''
    Функция для запросов, с помощью которых можно получить данные
    например SELECT и т.д.
    '''
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        try:
            record = cursor.fetchall()
            for rec in record:
                print(rec)
        except ProgrammingError as e:
            print(f'The error "{e}" occurred')
    except OperationalError as e:
        print(f'The error "{e}" occurred')


def main_console():
    command = input('Введите номер команды: \n'
                    '1 - Работа с получателями\n'
                    '2 - Работа с подписками\n'
                    '3 - Работа с изданиями\n'
                    'exit - выход из программы\n'
                    'Ваша команда : ')
    return command


def menu_poluchateli():
    command = input('Введите номер команды: \n'
                    '1 - Добавить нового получателя\n'
                    '2 - Удалить получателя\n'
                    '3 - Выбрать получателя\n'
                    '4 - Посмотреть всех получателей\n'
                    '5 - Выйти в предыдущее меню\n'
                    'exit - выход в главное меню\n'
                    'Ваша команда : ')
    return command


def new_poluchatel():
    kod_poluchatelya = input('Введите код получателя: ')
    fio = input('Введите ФИО получателя: ')
    address = input('Введите адрес получателя: ')
    query = f"INSERT INTO poluchatel VALUES ({kod_poluchatelya}, '{fio}', '{address}');"
    return query


def del_poluchatel():
    print('Вы собираетесь удалить получателя из базы данных\n')
    kod_poluchatelya = input('Введите код получателя, которого вы хотите удалить из базы данных: ')
    query = f"DELETE FROM poluchatel WHERE kod_poluchatelya = {kod_poluchatelya};"
    return query


def choose_poluchatel():
    kod_poluchatelya = input('Введите код получателя, информацию о котором вы хотите узнать: ')
    query = f"SELECT * FROM poluchatel WHERE kod_poluchatelya = {kod_poluchatelya};"
    return query


def all_poluchatel():
    query = f"SELECT * FROM poluchatel;"
    return query


def start_program():
    command = menu_poluchateli()
    while command != 'exit':
        if command == '1':
            execute_query(connection, new_poluchatel())
            print('Новый получатель добавлен')
            print()
            command = menu_poluchateli()
        elif command == '2':
            execute_query(connection, del_poluchatel())
            print('Получатель удален')
            print()
            command = menu_poluchateli()
        elif command == '3':
            fetchall_query(connection, choose_poluchatel())
            command = menu_poluchateli()
            print()
        elif command == '4':
            fetchall_query(connection, all_poluchatel())
            print()
            command = menu_poluchateli()


connection = create_connection('bel_post_2', 'postgres', '1234', '127.0.0.1', '5432')
start_program()
