class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root, targetSum):
    # Рекурсивная функция для проверки наличия пути с суммой targetSum
    def check_path(node, current_sum):
        if not node:  # Если узел не существует, возвращаем False
            return False
        if not node.left and not node.right:  # Если мы достигли листа
            return current_sum + node.val == targetSum  # Проверяем равенство суммы
        # Рекурсивно проверяем левое и правое поддеревья
        return (check_path(node.left, current_sum + node.val) or
                check_path(node.right, current_sum + node.val))

    # Начинаем проверку с корневого узла
    return check_path(root, 0) if root else False


# Пример использования:
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

targetSum = 22
print(has_path_sum(root, targetSum))  # Вывод: True

# Еще примеры:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
targetSum2 = 5
print(has_path_sum(root2, targetSum2))  # Вывод: False

root3 = None
targetSum3 = 0
print(has_path_sum(root3, targetSum3))  # Вывод: False
