class Que:
    def __init__(self):
        self.que = []

    # добавляем элемент в очередь:
    def push(self, n):
        self.que.insert(0, n)
        print('ok')

    # удаляем из очереди первый элемент:
    def pop(self):
        print(self.que.pop())

    # выводим первое значение элемента:
    def front(self):
        print(self.que[-1])

    # выводим размер очереди:
    def size(self):
        print(len(self.que))

    # очищаем очередь:
    def clear(self):
        self.que = []
        print('ok')

    # завершаем программу:
    def exit(self):
        print('bye')


if __name__ == '__main__':
    que = Que()
    que.size()
    que.push(1)
    que.size()
    que.push(2)
    que.size()
    que.push(3)
    que.size()
    que.exit()
