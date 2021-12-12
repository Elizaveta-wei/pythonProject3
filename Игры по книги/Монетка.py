import random

print("\tИгра 'Монетка'\n")
orel_1 = "orel"
reshka_1 = "reshka"
orel_sum = 0
reshka_sum = 0
count = 0
while count != 100:
    count += 1
    n = random.randint(1, 2)
    if n == 1:
        orel_sum += 1
    else:
        reshka_sum += 1
print("Орел:", orel_sum, "Решка:", reshka_sum)
