def str_float(x):
    try:
        print(float(x))
    except ValueError:
        print('вы мне передали не число')

str_float('42')
str_float('sfsdsdgfsg')
str_float('345.33')
