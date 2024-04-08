class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


# Пример использования
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = insert(root, key)

search_key = 40
result = search(root, search_key)

if result:
    print(f"Ключ {search_key} найден в дереве.")
else:
    print(f"Ключ {search_key} не найден в дереве.")
