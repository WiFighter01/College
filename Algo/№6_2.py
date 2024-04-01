def dfs(graph, visited, vertex):
    visited[vertex] = True
    count = 1  # Начинаем с учетом текущей вершины
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and not visited[neighbor]:
            count += dfs(graph, visited, neighbor)
    return count

# Пример входных данных
N, S = 3, 1
adjacency_matrix = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]

# Инициализируем массив для отслеживания посещенных вершин
visited = [False] * N

# Находим количество вершин в компоненте связности с вершиной S
result = dfs(adjacency_matrix, visited, S - 1)

# Выводим результат
print(result)