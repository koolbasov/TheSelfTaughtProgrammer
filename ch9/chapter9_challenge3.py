list_of_movies = [["Звёздные войны", "Терминатор", "Искусственный интеллект"],
                  ["Дурак", "Матильда", "Левиафан"],
                  ["Люди в чёрном", "Я робот", "Эволюция"]]

import csv

with open("movies.csv", "w", newline="", encoding="utf8") as f:
    w = csv.writer(f, delimiter=",")
    for i in list_of_movies:
        w.writerow(i)
