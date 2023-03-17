'''
Декораторы
'''
import time


def testTime(fn):
    def wrapper(*args, **kwargs):
        st = time.time()
        fn(*args, **kwargs)
        dt = time.time() - st
        print(f'Время работы: {dt} сек')

    return wrapper


@testTime
def getNOD(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@testTime
def getFastNOD(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


getNOD(100000, 2)

getFastNOD(100000, 2)

# def testTime(fn):
#     def wrapper(*args):
#         st = time.time()
#         fn(*args)
#         dt = time.time() - st
#         print(f'Время работы: {dt} сек')
#
#     return wrapper
#
#
# testTime(getNOD)(100000, 2)
# testTime(getFastNOD)(100000, 2)


# def testTime1(fn, *args):
#     st = time.time()
#     fn(*args)
#     dt = time.time() - st
#     print(f'Время работы: {dt} сек')
#
#
# testTime1(getNOD, 100000, 2)
