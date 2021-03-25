rock = []
country = []

def collect_songs():
    song = "Укажите песню. "
    ask = "Введите Р (рок) или К (кантри). Введите В для выхода: "
    while True:
        genre = input(ask)
        if genre == "В":
            break
        if genre == "Р":
            rk = input(song)
            rock.append(rk)
        elif genre == "К":
            cy = input(song)
            country.append(cy)
        else:
            print("Неверно")
    print(rock)
    print(country)

collect_songs()
