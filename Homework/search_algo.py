# 1. Бинарный поиск (итерация)
def binary_search(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[mid]
        if guess == val:
            return mid
        if guess > val:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print('1. Бинарный поиск (итерация):')
print(binary_search(my_list, 7))
print(binary_search(my_list, -1))
print()


# 2. Бинарный поиск (рекурсия)
def binary_search_recursive(arr, val, low, high):
    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[mid]
        if guess == val:
            return mid
        if guess > val:
            return binary_search_recursive(arr, val, low, mid - 1)
        else:
            return binary_search_recursive(arr, val, mid + 1, high)
    return None


my_list = [1, 3, 5, 7, 9]

print('2. Бинарный поиск (рекурсия):')
print(binary_search(my_list, 7))
print(binary_search(my_list, -1))
print()


# 3. Фибоначчиев поиск
def fibonacci_search(arr, val):
    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = fib_minus_1 + fib_minus_2
    while fib < len(arr):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2
    index = -1
    while fib > 1:
        i = min(index + fib_minus_2, len(arr) - 1)
        if arr[i] < val:
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            index = i
        elif arr[i] > val:
            fib = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib - fib_minus_1
        else:
            return i
    if fib_minus_1 and index < (len(arr) - 1) and arr[index + 1] == val:
        return index + 1
    return None


print('3. Фибоначчиев поиск:')
my_list = [1, 3, 5, 7, 9]
print(fibonacci_search(my_list, 7))
print(fibonacci_search(my_list, -1))
print()


# 4. Интерполяционный поиск
def interpolation_search(arr, val):
    low = 0
    high = (len(arr) - 1)
    while low <= high and val >= arr[low] and val <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (val - arr[low])))
        if arr[index] == val:
            return index
        if arr[index] < val:
            low = index + 1
        else:
            high = index - 1
    return None


print('4. Интерполяционный поиск:')
my_list = [1, 3, 5, 7, 9]
print(interpolation_search(my_list, 7))
print(interpolation_search(my_list, -1))