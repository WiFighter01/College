class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_balanced(root):
    """
    Функция для проверки сбалансированности дерева.
    Возвращает True, если дерево сбалансировано, иначе False.
    """
    if root is None:
        return True

    # Рекурсивно проверяем баланс поддеревьев
    left_height = height(root.left)
    right_height = height(root.right)

    if (abs(left_height - right_height) <= 1) and is_balanced(root.left) and is_balanced(root.right):
        return True

    return False


def height(node):
    """
    Вспомогательная функция для определения высоты дерева.
    """
    if node is None:
        return 0

    return max(height(node.left), height(node.right)) + 1


def sorted_array_to_bst(arr):
    """
    Функция для построения сбалансированного дерева из отсортированного массива.
    """
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])

    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid + 1:])

    return root


# Пример использования
if __name__ == "__main__":
    # Построение сбалансированного дерева из отсортированного массива
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = sorted_array_to_bst(arr)

    # Проверка на сбалансированность
    if is_balanced(root):
        print("Дерево сбалансировано")
    else:
        print("Дерево не сбалансировано")
