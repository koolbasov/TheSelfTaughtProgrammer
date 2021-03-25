lst = ["Ходячие мертвецы", "Красавцы", "Клан Сопрано", "Дневники вампира"]
# мой вариант:
for i in lst:
    print(i, lst.index(i))

print()

# вариант из книги
for index, show in enumerate(lst):
    print(index)
    print(show)
