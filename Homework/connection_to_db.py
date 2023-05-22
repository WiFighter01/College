import psycopg2
from psycopg2 import Error, OperationalError, ProgrammingError


# Функций подключения
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
        print()
    except OperationalError as e:
        print(f'The error "{e}" occurred')
        print()

    return connection


def execute_query(connection, query):
    '''
    Функция исполняет запрос в базе данных и в случае успешного выполнения выводит
    сообщение об успешном действии
    Для таких запросов как INSERT INTO и т.д.
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


# Главное меню программы
def main_menu():
    command = input('Введите номер команды: \n'
                    '1 - Работа с получателями\n'
                    '2 - Работа с подписками\n'
                    '3 - Работа с изданиями\n'
                    'exit - выход из программы\n'
                    'Ваша команда : ')
    print()
    return command


# Подменю "Получатель" и его функции
def menu_poluchateli():
    command = input('Введите номер команды: \n'
                    '1 - Добавить нового получателя\n'
                    '2 - Удалить получателя\n'
                    '3 - Выбрать получателя\n'
                    '4 - Посмотреть всех получателей\n'
                    '5 - Выйти в предыдущее меню\n'
                    'exit - выход в главное меню\n'
                    'Ваша команда : ')
    print()
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


# Подменю "Подписки" и его функции
def menu_podpiski():
    command = input('Введите номер команды: \n'
                    '1 - Добавить новою подписку\n'
                    '2 - Удалить подписку\n'
                    '3 - Выбрать подписку\n'
                    '4 - Посмотреть все оформленные подписки\n'
                    '5 - Выйти в предыдущее меню\n'
                    'exit - выход из программы\n'
                    'Ваша команда : ')
    print()
    return command


def new_podpiska():
    kod_poluchatelya = input('Введите код получателя: ')
    idx_izdaniya = input('Введите индекс издания: ')
    srok_podpiski = input('Введите срок подписки: ')
    while srok_podpiski not in (1, 3, 6):
        print('Доступный срок подписки: 1, 3 или 6 месяцев\n')
        srok_podpiski = input('Введите срок подписки: ')
    month = input('Введите месяц начала доставки издания: ')
    while month not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        print('Диапазон месяцев от 1 до 12\n')
        month = input('Введите месяц начала доставки издания: ')
    year = input('Введите год начала доставки издания: ')
    query = f"INSERT INTO podpiski VALUES ({kod_poluchatelya}, {idx_izdaniya}, {srok_podpiski}, {month}, {year});"
    return query


def del_podpiska():
    print('Вы собираетесь удалить подписку из базы данных\n')
    kod_poluchatelya = input('Введите код получателя, подписку которого вы хотите удалить из базы данных: ')
    idx_izdaniya = input('Введите индекс издания, на которое оформлена подписка: ')
    query = f"DELETE FROM podpiski WHERE kod_poluchatelya = {kod_poluchatelya} AND idx_izdaniya = {idx_izdaniya};"
    return query


def choose_podpiska():
    kod_poluchatelya = input('Введите код получателя, информацию о подписке которого вы хотите узнать: ')
    idx_izdaniya = input('Введите индекс издания, на которое оформлена подписка получателя: ')
    query = f"SELECT * FROM podpiski WHERE kod_poluchatelya = {kod_poluchatelya} AND idx_izdaniya = {idx_izdaniya};"
    return query


def all_podpiska():
    query = f"SELECT * FROM podpiski;"
    return query


# Подменю "Издания" и его функции
def menu_izdaniya():
    command = input('Введите номер команды: \n'
                    '1 - Добавить новою издание\n'
                    '2 - Удалить издание\n'
                    '3 - Выбрать издание\n'
                    '4 - Посмотреть все доступные для подписки издания\n'
                    '5 - Выйти в предыдущее меню\n'
                    'exit - выход из программы\n'
                    'Ваша команда : ')
    print()
    return command


def new_izdaniya():
    idx_izdaniya = input('Введите индекс издания: ')
    vid_izdaniya = input('Введите вид издания: ')
    name_izdaniya = input('Введите название издания: ')
    price = input('Введите стоимость подписки на издание на 1 мес.: ')
    query = f"INSERT INTO izdaniya VALUES ({idx_izdaniya}, '{vid_izdaniya}', '{name_izdaniya}', {price});"
    return query


def del_izdaniya():
    print('Вы собираетесь удалить издание из базы данных\n')
    idx_izdaniya = input('Введите индекс издания, которое вы хотите удалить: ')
    query = f"DELETE FROM izdaniya WHERE idx_izdaniya = {idx_izdaniya};"
    return query


def choose_izdaniya():
    idx_izdaniya = input('Введите индекс издания, информацию о котором вы хотите узнать: ')
    query = f"SELECT * FROM izdaniya WHERE idx_izdaniya = {idx_izdaniya};"
    return query


def all_izdaniya():
    query = f"SELECT * FROM izdaniya;"
    return query


# Функция запуска программы
def start_program():
    # Вызываем главное меню и не завершаем программу пока пользователь
    # Не введет 'exit'
    command = main_menu()
    while command != 'exit':
        # Вызываем подменю "Получатель"
        if command == '1':
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
                elif command == '5':
                    command = main_menu()
                    break
                elif command == 'exit':
                    command = 'exit'
        # Вызываем подменю "Подписки"
        elif command == '2':
            command = menu_podpiski()
            while command != 'exit':
                if command == '1':
                    execute_query(connection, new_podpiska())
                    print('Новый подписка добавлена')
                    print()
                    command = menu_podpiski()
                elif command == '2':
                    execute_query(connection, del_podpiska())
                    print('Подписка удалена')
                    print()
                    command = menu_podpiski()
                elif command == '3':
                    fetchall_query(connection, choose_podpiska())
                    command = menu_podpiski()
                    print()
                elif command == '4':
                    fetchall_query(connection, all_podpiska())
                    print()
                    command = menu_podpiski()
                elif command == '5':
                    command = main_menu()
                    break
                elif command == 'exit':
                    command = 'exit'
        # Вызываем подменю "Издания"
        elif command == '3':
            command = menu_izdaniya()
            while command != 'exit':
                if command == '1':
                    execute_query(connection, new_izdaniya())
                    print('Новое издание добавлено')
                    print()
                    command = menu_izdaniya()
                elif command == '2':
                    execute_query(connection, del_izdaniya())
                    print('Издание удалено')
                    print()
                    command = menu_izdaniya()
                elif command == '3':
                    fetchall_query(connection, choose_izdaniya())
                    command = menu_izdaniya()
                    print()
                elif command == '4':
                    fetchall_query(connection, all_izdaniya())
                    print()
                    command = menu_izdaniya()
                elif command == '5':
                    command = main_menu()
                    break
                elif command == 'exit':
                    command = 'exit'


connection = create_connection('bel_post_2', 'postgres', '1234', '127.0.0.1', '5432')
start_program()
