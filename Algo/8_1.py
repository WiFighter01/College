class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        if isinstance(child, TreeNode):
            self.children.append(child)
        else:
            print("Child must be a TreeNode instance.")

    def __repr__(self, level=0):
        ret = "  " * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


# Создаем узлы
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

# Добавляем детей к корневому узлу
root.add_child(b)
root.add_child(c)

# Добавляем детей к узлу B
b.add_child(d)
b.add_child(e)

# Выводим дерево
print(root)
