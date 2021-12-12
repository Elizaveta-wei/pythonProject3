print("Введите текст, а мы напечатаем его наооборот!")
a = input()
while a:
    print(a[len(a)-1], end='')
    a = a[:(len(a) - 1)]
input('\n\nНажмите Enter, чтобы выйти')
