me = {"имя": "Брюс",
      "фамилия": "Ли",
      "рост": "170",
      "вес": "70"}


answer = input("Укажите имя, фамилию, рост или вес: ")
if answer in me:
    result = me[answer]
    print(result)
