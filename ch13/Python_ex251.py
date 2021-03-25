# Не выполнять

# Рисование фигур
# без полиморфизма
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if type(a_shape) == "Треугольник":
        a_shape.draw_triangle()
    if type(a_shape) == "Квадрат":
        a_shape.draw_square()
    if type(a_shape) == "Круг":
        a_shape.draw_circle()

# Рисуем фигуры
# c помощью полиморфизма
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    a_shape.draw()
