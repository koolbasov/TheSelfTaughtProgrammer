# Создайте класс Circle с методом area, подсчитывающим и возвращающим
# площадь круга. Затем создайте объект Circle, вызовите в нем метод area и
# выведите результат. Воспользуйтесь функцией pi из встроенного в Python
# модуля math.

import math
class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

for i in range(1, 11):
    circle = Circle(i)
    print(circle.area())
        
