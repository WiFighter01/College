class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Значение узла
        self.left = left  # Левый потомок
        self.right = right  # Правый потомок


def max_path_sum(root):
    # Инициализируем переменную для хранения максимальной суммы пути
    max_sum = float('-inf')

    # Определяем вспомогательную рекурсивную функцию для вычисления максимальной суммы пути
    def max_path_sum_helper(node):
        nonlocal max_sum
        if not node:
            return 0

        # Вычисляем максимальную сумму пути для левого и правого поддеревьев
        left_sum = max(0, max_path_sum_helper(node.left))
        right_sum = max(0, max_path_sum_helper(node.right))

        # Обновляем максимальную сумму пути, если текущий путь через узел больше
        max_sum = max(max_sum, left_sum + right_sum + node.val)

        # Возвращаем максимальную сумму пути, которая может быть продолжена из текущего узла
        return max(left_sum, right_sum) + node.val

    # Начинаем рекурсию с корневого узла
    max_path_sum_helper(root)

    return max_sum


# Пример использования:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(max_path_sum(root))  # Вывод: 6
