import random

print('\tПирожок с сюрпризом')
print('Посмотри какой выпадет тебе\n')
n = random.randint(1, 5)
if n == 1:
    print("Тебя ждет замечательный день")
elif n == 2:
    print("Давай работай больше")
elif n == 3:
    print("Пора пахать в СП")
elif n == 4:
    print("Вот это денек - мяу")
elif n == 5:
    print("Опять работать")
else:
    print("Чет не прет")
input('\nНажмите Enter чтобы выйти')
