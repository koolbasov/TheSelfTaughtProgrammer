# Создайте класс Shape. Определите в нем метод what_am_i, который при вы-
# зове выводит строку "Я - фигура" Измените ваши классы Rectangle и
# Square из предыдущих заданий для наследования от Square, создайте объек-
# ты Square и Rectangle и вызовите в них новый метод.

class Shape():
    def what_am_i(self):
        print("Я - фигура")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

        

rectangle = Rectangle(25, 50)
square = Square(20)

rectangle.what_am_i()
square.what_am_i()

