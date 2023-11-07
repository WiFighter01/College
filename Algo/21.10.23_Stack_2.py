# Задача 2

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print('ok')

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        print(removed)

    def back(self):
        print(self.stack[-1])

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack = []
        print('ok')

    def exit(self):
        print('bye')


s = Stack()
s.push(3)
s.push(14)
s.size()
s.clear()
s.push(1)
s.back()
s.push(2)
s.back()
s.pop()
s.size()
s.pop()
s.size()
s.exit()
