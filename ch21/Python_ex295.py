# В этом примере вы построите очередь, используя четыре метода: enqueue,
# dequeue, is_empty и size. enqueue добавляет новый элемент в очередь; dequeue
#удаляет элемент из очереди; is_empty проверяет, пуста ли очередь, и возвращает со-
# ответственно True либо False; size возвращает количество элементов в очереди.

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Если вы создадите новую пустую очередь, метод is_empty вернет значение
# True.

a_queue = Queue()
print(a_queue.is_empty())
print()

# Добавьте в очередь элементы и узнайте ее размер.
a_queue = Queue()
for i in range(5):
    a_queue.enqueue(i)

print(a_queue.size())
print()

# Удалите каждый элемент из очереди.
a_queue = Queue()
for i in range(5):
    a_queue.enqueue(i)

for i in range(5):
    print(a_queue.dequeue())

print()
print(a_queue.size())






















