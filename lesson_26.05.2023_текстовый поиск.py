# # Алгоритмы поиска текстовой информации
# def test(text, pattern):
#     if not pattern:
#         print('Шаблон пустой')
#         return False
#     if not text:
#         print('Текст пустой')
#         return False
#     if len(pattern) > len(text):
#         print('Текст короче шаблона')
#         return False
#     return True
#
#
# # O(n*m)
# def find(text, pattern):
#     n = len(text)
#     m = len(pattern)
#     i = 0
#     finded = False
#     while i <= n - m:
#         for j in range(m):
#             if text[i + j] != pattern[j]:
#                 break
#         else:
#             finded = True
#             print('Шаблон найден по индексу ', i)
#             # i = n для поиска только первого вхождения
#         i += 1
#     if not finded:
#         print('Шаблон не найден')
#         # T = AAAAAAAAAA, P = AAAB
#
#
# # Метод КМП
# # O(n+m)
# def KMP(text, pattern):
#     n = len(text)
#     m = len(pattern)
#     char = list(pattern)
#     next_ind = [0] * (m + 1)
#
#     for i in range(1, m):
#         j = next_ind[i]
#         while j > 0 and char[j] != char[i]:
#             j = next_ind[j]
#         if j > 0 or char[j] == char[i]:
#             next_ind[i + 1] = j + 1
#
#     print('start')
#     i, j = 0, 0
#     finded = False
#     while i < n:
#         if j < m and text[i] == pattern[j]:
#             j = j + i
#             if j == m:
#                 finded = True
#                 print('Шаблон найден по индексу', (i - j + 1))
#         elif j > 0:
#             j = next_ind[j]
#             i = i - 1
#         i = i + 1
#     if not finded:
#         print('Шаблон не найден')


# Метод КМП из видео
# O(n+m)
t = "лилила"

p = [0]*len(t)
j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        p[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0;
            i += 1
        else:
            j = p[j-1]

print(p)

a = "лилилось лилилась"
m = len(t)
n = len(a)

i = 0
j = 0
while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("образ найден")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1

if i == n and j != m:
    print("образ не найден")


# if __name__ == '__main__':
#     text = 'ABCABAABCABAC'
#     pattern = 'CAB'
#     if test(text, pattern):
#         # find(text, pattern)
#         KMP(text, pattern)



