# 1. Реализовать метод getMax(), который возвращает значение, являющееся максимальным для заданного стека на текущий
# момент. В случае, если стек пустой, то вернуть None

class Stack:
    def __init__(self):
        self.stack = []
        # Создаем отдельный список, в котором будет храниться только одно максимальное значение стека
        self.stack_max = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def push(self, item):
        self.stack.append(item)
        # добавляем максимальное значение если его еще не было
        if len(self.stack_max) == 0:
            self.stack_max.append(item)
        else:
            # сравниваем текущее максимальное значение с item и меняем, если item больше
            if item > self.stack_max[0]:
                self.stack_max[0] = item

    def get_max(self):
        return self.stack_max[0]


s = Stack()

s.push(1)
s.push(7)
s.push(100)
s.push(20)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print()
print("Максимум в стеке: ", s.get_max())
