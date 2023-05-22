from math import sqrt

EPS = 0.0000000000000001


def square_eq_solver(a, b, c):
    result = []
    D = b ** 2 - 4 * a * c
    if abs(D) < EPS:
        result.append(-b / (2 * a))
    elif D > 0:
        result.append((-b + sqrt(D)) / (2 * a))
        result.append((-b - sqrt(D)) / (2 * a))
    return result


def show_result(data):
    if len(data) > 0:
        for ind, val in enumerate(data):
            print(f"Корень номер {ind + 1} равен {val:.02f}")
    else:
        print('Уравнение с заданными параметрами не имеет корней')


def main():
    a, b, c = map(int, input("Введите три числа через пробел: ").split())
    res = square_eq_solver(a, b, c)
    show_result(res)


def test_no_root():
    res = square_eq_solver(10, 0, 2)
    assert len(res) == 0


def test_single_root():
    res = square_eq_solver(10, 0, 0)
    assert len(res) == 1
    assert res == [0]


def test_multiple_root():
    res = square_eq_solver(2, 5, -3)
    assert len(res) == 2
    assert res == [0.5, -3]  # -3.00000000023


if __name__ == '__main__':
    main()
