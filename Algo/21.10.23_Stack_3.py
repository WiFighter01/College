# Задача 3

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print('ok')

    def pop(self):
        if len(self.stack) == 0:
            print('error')
        else:
            removed = self.stack.pop()
            print(removed)

    def back(self):
        if len(self.stack) == 0:
            print('error')
        else:
            print(self.stack[-1])

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack = []
        print('ok')

    def exit(self):
        print('bye')


s = Stack()
s.size()
s.push(1)
s.size()
s.push(2)
s.size()
s.push(3)
s.size()
s.exit()
