'''
TDD - разработка управляемая тестами
'''


def convfrom10(dnum: int, nbase: int = 2):
    '''
    Перевод числа dnum из десятичной системы счисления в систему счисления с основанием nbase.
    dnum должно быть >= 0
    2 <= nbase < 10
    Если не указано основание СС, то по умолчанию оно равно 2.
    Функция возвращает строку, в которой записано число в новой СС с префиксом
    'nbase_', если dnum < 0, то возвращаем перевод модуля с "-" вначале.

    :param dnum: число в десятичной СС
    :param nbase: основание СС
    :return: строка с числом в новой СС
    '''
    if type(dnum) != int or dnum < 0:
        return 'первый аргумент - целое неотрицательное число'
    if type(nbase) != int or nbase < 2 or nbase > 9:
        return 'второй аргумент - целое число >= 2 и < 10'
    if dnum == 0:
        return f'{nbase}_0'
    res = ''
    while dnum != 0:
        res = str(dnum % nbase) + res
        dnum //= nbase
    return f'{nbase}_{res}'


def test_convfrom10():
    # test1 - значение по умолчанию
    if convfrom10(14) == '2_1110':
        print('test1 - ok')
    else:
        print('test1 - fail')
    # test2 - общий вызов
    if convfrom10(14, 8) == '8_16':
        print('test2 - ok')
    else:
        print('test2 - fail')
    # test3 - граничное значение
    if convfrom10(0) == '2_0':
        print('test3 - ok')
    else:
        print('test3 - fail')
    # test4 - неправильный первый аргумент
    if convfrom10(-2) == 'первый аргумент - целое неотрицательное число':
        print('test4 - ok')
    else:
        print('test4 - fail')
    # test5 - неправильный второй аргумент
    if convfrom10(2, -3) == 'второй аргумент - целое число >= 2 и < 10':
        print('test5 - ok')
    else:
        print('test5 - fail')
    # test6 - nbace > 10
    if convfrom10(2, 16) == 'второй аргумент - целое число >= 2 и < 10':
        print('test6 - ok')
    else:
        print('test6 - fail')
    # test7 - dnum не целое чило
    if convfrom10(2.2, 16) == 'первый аргумент - целое неотрицательное число':
        print('test7 - ok')
    else:
        print('test7 - fail')


if __name__ == '__main__':
    test_convfrom10()
