# Определите класс Apple с четырьмя переменными экземпляра, представля-
# ющими четыре свойства яблока.
class Apple():
    def __init__(self, weight, diametr, color, sort):
        self.weight = weight
        self.diametr = diametr
        self.color = color
        self.sort = sort
        print("Cоздано!")

app1 = Apple(100, 100, 'red', 'antonovka')
print(app1.weight)
print(app1.diametr)
print(app1.color)
print(app1.sort)
