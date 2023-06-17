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
print('1. Алгоритм поиска в ширину:')
search('you')
print()

# 2. Алгоритм Дейкстры
# Граф
graph_2 = {}
graph_2["start"] = {}
graph_2["start"]["a"] = 6
graph_2["start"]["b"] = 2

graph_2["a"] = {}
graph_2["a"]["fin"] = 1

graph_2["b"] = {}
graph_2["b"]["a"] = 3
graph_2["b"]["fin"] = 5

graph_2["fin"] = {}

# Таблица стоимости
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Таблица родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Проход через каждый узел
    for node in costs:
        cost = costs[node]
        # Если это самая низкая стоимость на данный момент и она еще не была обработана...
        if cost < lowest_cost and node not in processed:
            # ... установите его в качестве нового узла с наименьшими затратами.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# Найдите узел с наименьшими затратами, который вы еще не обработали.
node = find_lowest_cost_node(costs)
# Если вы обработали все узлы, этот цикл while завершен.
while node is not None:
    cost = costs[node]
    # Пройдите через всех соседей этого узла.
    neighbors = graph_2[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Если дешевле добраться до этого соседа, пройдя через этот узел...
        if costs[n] > new_cost:
            # ... обновите стоимость для этого узла.
            costs[n] = new_cost
            # Этот узел становится новым родительским для этого соседа.
            parents[n] = node
    # Отметьте узел как обработанный.
    processed.append(node)
    # Найдите следующий узел для обработки и выполните цикл.
    node = find_lowest_cost_node(costs)

print('2. Алгоритм Дейкстры:')
print("Стоимость начиная от старта до каждого узла:")
print(costs)
