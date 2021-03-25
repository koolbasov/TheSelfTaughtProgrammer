x = [66, 8, 15, 34, 88, 99]

while True:
    answer = input("Введите число или X чтобы выйти: ")
    if answer == "X":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("пожалуйста, введите число или Х для выхода.")
    if answer in x:
        print("Ура! Вы угадали число из списка!")
    else:
        print("Вы не угадали чилос из списка")
        
