# 1. Поиск в ширину
from collections import deque


# Вспомогательная функция определяющая необходимого персонажа
def person_is_it(name):
    return name[:2] == 'Pe'


# Сам алгоритм
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_it(person):
                print(f'{person} is founded')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {'you': ['Alice', 'Bob', 'Clar'], 'Bob': ['Anudj'], 'Alice': ['Peggi'], 'Clar': ['Tom', 'Jonny'],
         'Peggi': ['Bob']}
search('you')

# 2. Алгоритм Дейкстры
