# Создайте классы Horse и Rider. Используйте композицию, чтобы смодели-
# ровать лошадь с всадником на ней.

class Horse():
    def __init__(self, name, breed, owner):
        self.name  = name
        self.breed = breed
        self.owner = owner

class Rider():
    def __init__(self, name):
        self.name = name



ivan = Rider('Иван Дурак')
sivka = Horse('Сивка Бурка', 'мустанг', ivan)

print(sivka.name +",", "порода:", sivka.breed + ",", "хозяин:", sivka.owner.name)
