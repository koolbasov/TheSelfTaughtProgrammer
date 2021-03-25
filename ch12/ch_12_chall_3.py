# Создайте класс Triangle с методом area, подсчитывающим и возвращаю-
# щим площадь треугольника. Затем создайте объект Triangle, вызовите в
# нем area и выведите результат.

import math
class Triangle():
    def __init__(self, side1, side2, angle):
        self.side1 = side1
        self.side2 = side2
        self.angle = angle

    def area(self):
        return 1/2 * self.side1 * self.side2 * math.sin(math.radians(self.angle))

triangle = Triangle(8, 9, 30)
print(triangle.area())
