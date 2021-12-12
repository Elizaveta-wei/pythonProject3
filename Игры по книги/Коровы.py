# Счетчик коров

n = int(input())
if 10 < n < 20 or n % 10 == 0 or n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9:
    print("Коров")
elif n == 1 or n % 10 == 1:
    print("Корова")
else:
    print("Коровы")
