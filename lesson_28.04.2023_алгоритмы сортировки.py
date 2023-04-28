# Сортировка выбором
array = [5, 11, 6, 4, 9, 2, 15, 7]
for j in range(0, len(array) - 1):
    nmin = array[j]
    ind = j
    for i in range(j, len(array)):
        if array[i] < nmin:
            nmin = array[i]
            ind = i
    array[ind] = array[j]
    array[j] = nmin
print(array)

# Сортировка вставками
# Не делали, надо самим сделать

# Сортировка пузырьком
# Надо добавить flag на то, есть ли замена элементов в очередной итерации
# Если нет, то завершать цикл
array2 = [40, 11, 83, 57, 32, 21, 75, 64]
for i in range(len(array2) - 1):
    for j in range(0, (len(array2) - 1) - i):
        if array2[j+1] < array2[j]:
            array2[j], array2[j+1] = array2[j+1], array2[j]
print(array2)

# Сортировка слияниями
# Не делали, надо самим сделать


# Сортировка шейкерная
# Не делали, надо самим сделать


# Сортировка метод Шелла
# Не делали, надо самим сделать

# Сортировка метод Хоара
# Не делали, надо самим сделать

