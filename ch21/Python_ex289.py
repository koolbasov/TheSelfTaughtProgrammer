class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

# Если вы создадите новый стек, он будет пуст, и метод is_empty вернет зна-
# чение True.
stack = Stack()
print(stack.is_empty())
print()

# Если вы добавите новый элемент в стек, метод is_empty вернет значение
# False.
stack = Stack()
stack.push(1)
print(stack.is_empty())
print()

# Вызовите метод pop, чтобы удалить элемент из стека, тогда метод is_empty
# снова вернет значение True.
stack = Stack()
stack.push(1)
item = stack.pop()
print(item)
print(stack.is_empty())
print()

# Наконец, вы можете заглянуть в содержимое стека и узнать его размер.
stack = Stack()

for i in range(0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())
print()






















