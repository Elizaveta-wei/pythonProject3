import random

# создаем последовательности слов, из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстоканник")
# случаным образом выберем из последовательности одно слово
word = random.choice(WORDS)
# создадим переменную: с которой будет затем сопоставлена версия игрока
correct = word

# создадим анаграмму выбранного слова, в которой буквы бубут расставлены хаотично
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
print(
    """
               Добро пожалловать в игрц "Анаграммы"!

           Надо перставить буквы так, чтобы получилось осмысленное слово.
    (Для входа нажмите Enter, не вводя своей версии.)
    """
)
print("Вот анаграмма:", jumble)

guess = input("\nПопробуй отгадать исходное слово: ")
while guess != correct and guess != "":
    print("К сожалению, вы не правы.")
    podskaska = input("Не хотите взять подсказку?")
    if podskaska.lower() == "Да":
        i = 0
        print(word[i])
        i += 1
    elif podskaska.lower() == "Нет":
        guess = input("Попробуй отгадать исходное слово: ")
    else:
        guess = input("Попробуй отгадать исходное слово: ")
if guess == correct:
    print("Да, именно так! Вы отгадали!\n")

print("Спасибо за игру.")

input("\n\nPress the enter key to exit.")
