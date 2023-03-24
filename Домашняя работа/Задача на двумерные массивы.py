from random import randint


def matrix(n: int, m: int, a: int = 1, b: int = 3):
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

def minus_m(a, b):
    '''
    Вычитаем матрицы a и b
    '''
    res = []
    for i in range(len(a)):
        res.append([])
        for j in range(len(a[i])):
            res[i].append(a[i][j] - b[i][j])
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

def mult_m_2(a, b: int):
    '''
    Перемножаем матрицу a на число b
    '''
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= b
    return a

def opred_2(a):
    '''
    Вычисляем определитель второго порядка для квадратной матрицы a
    '''
    res = a[0][0]*a[1][1] - a[0][1]*a[1][0]
    return res


# умножение матриц
a1 = matrix(3, 2)
a2 = matrix(2, 3)
print_m(a1)
print('*')
print_m(a2)
print('=')
print_m(mult_m(a1, a2))
print()

# Вычитание матриц
b1 = matrix(3, 3)
b2 = matrix(3, 3)
print_m(b1)
print('-')
print_m(b2)
print('=')
print_m(minus_m(b1, b2))
print()

# Умножение матрицы на число
c1 = matrix(4, 2)
c2 = 5
print_m(c1)
print('*')
print(c2)
print('=')
print_m(mult_m_2(c1, c2))
print()

# Определитель 2 порядка
d1 = matrix(2, 2)
print_m(d1)
print('определитель матрицы равен =', opred_2(d1))
