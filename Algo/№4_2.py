class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        raise IndexError("Index out of range")

    def remove(self, index):
        current = self.head
        if index == 0:
            self.head = current.next
            return
        prev = None
        count = 0
        while current and count != index:
            prev = current
            current = current.next
            count += 1
        if current is None:
            raise IndexError("Index out of range")
        prev.next = current.next

    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        prev_ptr = None
        while fast_ptr and fast_ptr.next:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if fast_ptr is None:
            # Чётное количество элементов
            return prev_ptr.data, slow_ptr.data
        else:
            # Нечётное количество элементов
            return slow_ptr.data

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return '[' + ' '.join(elements) + ']'

# Пример использования:
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)
print('Текущий список:', my_list)
middle = my_list.find_middle()
if isinstance(middle, tuple):
    print('Средние элементы:', middle[0], middle[1])
else:
    print('Средний элемент:', middle)
