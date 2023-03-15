def convfrom10(dnum: int, nbase: int = 2):
    '''
    Перевод числа dnum из десятичной системы счисления в систему счисления с основанием nbase.
    dnum должно быть >= 0
    2 <= nbase <= 16
    Если не указано основание СС, то по умолчанию оно равно 2.
    Функция возвращает строку, в которой записано число в новой СС с префиксом
    'nbase_'.

    :param dnum: число в десятичной СС
    :param nbase: основание СС
    :return: строка с числом в новой СС
    '''
    if type(dnum) != int or dnum < 0:
        return 'первый аргумент - целое неотрицательное число'
    if type(nbase) != int or nbase < 2 or nbase > 16:
        return 'второй аргумент - целое число >= 2 и <= 16'
    if dnum == 0:
        return f'{nbase}_0'
    res = ''
    while dnum != 0:
        if dnum % nbase == 10:
            res = 'A' + res
        elif dnum % nbase == 11:
            res = 'B' + res
        elif dnum % nbase == 12:
            res = 'C' + res
        elif dnum % nbase == 13:
            res = 'D' + res
        elif dnum % nbase == 14:
            res = 'E' + res
        elif dnum % nbase == 15:
            res = 'F' + res
        else:
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
    if convfrom10(2, -3) == 'второй аргумент - целое число >= 2 и <= 16':
        print('test5 - ok')
    else:
        print('test5 - fail')
    # test6 - nbace > 16
    if convfrom10(2, 17) == 'второй аргумент - целое число >= 2 и <= 16':
        print('test6 - ok')
    else:
        print('test6 - fail')
    # test7 - dnum не целое чило
    if convfrom10(2.2, 16) == 'первый аргумент - целое неотрицательное число':
        print('test7 - ok')
    else:
        print('test7 - fail')
    # test8 - nbace > 10
    if convfrom10(23, 12) == '12_1B':
        print('test8 - ok')
    else:
        print('test8 - fail')


if __name__ == '__main__':
    test_convfrom10()