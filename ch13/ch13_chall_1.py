# Создайте классы Rectangle и Square с методом calculate_perimeter,
# вычисляющим периметр фигур, которые эти классы представляют. Создай-
# те объекты Rectangle и Square вызовите в них этот метод.

class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def r_perimeter(self):
        return (self.width + self.length) * 2

class Square():
    def __init__(self, side):
        self.side = side

    def s_perimeter(self):
        return self.side * 4

rectangle = Rectangle(6, 4)
square = Square(6)

print(rectangle.r_perimeter())
print(square.s_perimeter())
