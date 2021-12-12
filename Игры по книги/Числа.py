a = int(input('Введите начало счета:'))
b = int(input('Введите конец счета:'))
c = int(input('Введите интервал счета:'))
for i in range(a, b, c):
    print(i, end=" ")
input("\n\nНажмите Enter, чтобы выйти")
