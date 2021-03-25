#Измените класс Square так, чтобы когда вы выводите объект Square, выво-
#дилось сообщение с длинами всех четырех сторон фигуры. Например, если
#вы создадите квадрат при помощи Square(29) и осуществите вывод, Python
#должен вывести строку 29 на 29 на 29 на 29

class Square():

    def __init__(self, side):
        self.side = side
        
    def __repr__(self):
        return """Я квадрат {} на {} на {} на {}""".format(self.side,
                                                self.side,
                                                self.side,
                                                self.side)

square = Square(100)
print(square)
