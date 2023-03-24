from random import randint


def matrix(n: int, m: int, a: int = 0, b: int = 1):
    '''
    Генерирует матрицу размера n (кол-во строк) на m (кол-во столбцов),
    заполненную случайными числами в диапазоне от a до b
    '''
    return [[randint(a, b) for i in range(m)] for j in range(n)]


def print_m(a):
    '''
    Печатаем матрицу а по строкам
    '''
    for str_m in a:
        print(*str_m)


def sum_m(a, b):
    '''
    Суммируем матрицы a и b
    '''
    res = []
    for i in range(len(a)):
        res.append([])
        for j in range(len(a[i])):
            res[i].append(a[i][j] + b[i][j])
    return res


def mult_m(a, b):
    '''
    Перемножаем матрицы a и b
    '''
    n = len(a)
    m = len(b[0])
    k = len(b)  # len(a[0])
    res = [[0] * m for j in range(n)]
    for i in range(n):
        for j in range(m):
            for x in range(k):
                res[i][j] += a[i][x] * b[x][j]
    return res


a1 = matrix(3, 2)
a2 = matrix(2, 5)
print_m(a1)
print('*')
print_m(a2)
print('=')
print_m(mult_m(a1, a2))
