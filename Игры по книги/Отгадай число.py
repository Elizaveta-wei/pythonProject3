import random

print("\tОтгадай число\n")
print("У вас есть 6 попытки\n")
tries = ""
tries_n = 0
n = int(random.randint(1, 100))
while tries != n:
    if tries_n >= 6:
        print("Вы не угодали число! Его номер", n)
        break
    tries = int(input("Введите число:"))
    if tries > n:
        print("Меньше")
    elif tries < n:
        print("Больше")
    else:
        print("Конец, Вы сделали это!")
    tries_n += 1
if tries == n:
    print("Число было", n, ". Вы угодали с помощью", tries_n, "попыток. Хорошая работа!")
