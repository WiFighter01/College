'''
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.
'''
words = {}
x = int(input())
for i in range(x):
    words.update([input().split()])
value = input()
for key in words:
    if words[key] == value:
        print(key)
    elif key == value:
        print(words[key])
