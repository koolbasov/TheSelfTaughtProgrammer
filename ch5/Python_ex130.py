colors = ['фиолетовый',
          'оранжевый',
          'зеленый']

while True:
    guess = input("Угадайте цвет: ")
    if guess in colors:
        print("Вы угадали!")
        break
    elif guess == "exit":
        break
    else:
        print("Неправильно! Попробуйте еще. Для выхода напишите exit")
        continue
    
