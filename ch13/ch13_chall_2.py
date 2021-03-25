# В классе Square определите метод change_size, позволяющий передавать
# ему число, которое увеличивает или уменьшает (если оно отрицательное)
# каждую сторону объекта Square на соответствующее значение.

class Square():
    def __init__(self, side):
        self.side = side

    def change_size(self, ch_side):
        return self.side + ch_side

    def s_perimeter(self):
        return self.side * 4

square = Square(6)
print(square.change_size(4))
print(square.s_perimeter())

# пример из книги
class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)

