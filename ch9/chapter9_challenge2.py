answer = input('Введите все что взбредет вам в голову: ')

with open('nonsense.txt', 'w', encoding='utf-8') as f:
    f.write(answer)

print('Мы записали ваш ответ в файл nonsense.txt')
