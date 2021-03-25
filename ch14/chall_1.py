# Добавьте переменную square_list в класс Square так, чтобы всякий раз,
# когда вы создаете новый объект Square, он добавлялся в список.

class Square():
    square_list = []

    def __init__(self, x):
        self.x = x
        self.square_list.append(x ** 2)
        
    def squares(self):
        return self.x ** 2

s1 = Square(2)
print(s1.squares())
s2 = Square(4)
print(s2.squares())
s3 = Square(6)
print(s3.squares())

print(s3.square_list)
