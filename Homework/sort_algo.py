# 1. Сортировка выбором
# Функция для нахождения минимального индекса
def find_smallest(arr: list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# Cам алгоритм
def selection_sort(arr: list):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


arr = [5, 3, 11, 24, 6, 3, 10]
print('1. Сортировка выбором:')
print(selection_sort(arr))
print()


# 2. Сортировка вставкой
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = [5, 3, 11, 24, 6, 3, 10]
print('2. Сортировка вставками:')
print(insertion_sort(arr))
print()


# 3. Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


arr = [5, 3, 11, 24, 6, 3, 10]
print('3. Сортировка слиянием:')
print(merge_sort(arr))
print()


# 4. Сортировка обменом (пузырек)
def bubble_sort(arr):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # Меняем элементы
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return arr


arr = [5, 3, 11, 24, 6, 3, 10]
print('4. Сортировка обменом:')
print(bubble_sort(arr))
print()


# 5. Шейкерная сортировка
def cocktail_sort(arr):
    left = 0
    right = len(arr) - 1
    swapped = True
    while swapped:
        swapped = False
        # Проход слева направо (аналог прохода вперед в сортировке пузырьком)
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        right -= 1

        # Проход справа налево (аналог прохода назад в сортировке пузырьком)
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        left += 1
    return arr


arr = [5, 3, 11, 24, 6, 3, 10]
print('5. Шейкерная сортировка:')
print(cocktail_sort(arr))
print()


# 6. Сортировка Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i

            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = key

        gap //= 2

    return arr


arr = [5, 3, 11, 24, 6, 3, 10]
print('6. Сортировка Шелла:')
print(shell_sort(arr))
print()


# 7. Быстрая сортировка
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for i in range(1, len(arr)):
            if arr[i] <= pivot:
                less.append(arr[i])
            else:
                greater.append(arr[i])

        return quicksort(less) + [pivot] + quicksort(greater)


arr = [5, 3, 11, 24, 6, 3, 10]
print('7. Быстрая сортировка>:')
print(quicksort(arr))
