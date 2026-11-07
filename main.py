"""import random
num = str(random.randint(1000,9999))
guess = input("Введите четырёхзначное число: ")
while guess != num:
    bulls = 0
    cows = 0
    used = []
    for i in range(4):
        if guess[i] == num[i]:
            bulls += 1
            used.append(i)
    for i in range(4):
        if (guess[i] in num) and (guess[i] != num[i]):
            for j in range(4):
                if (guess[i] == num[j]) and (j not in used):
                    cows += 1
                    used.append(j)
                    break
    print(f"Быки: {bulls}, Коровы: {cows}")
    guess = input("Попробуйте еще раз: ")
print("Вы угадали")"""

""" import math
x = float(input("Введите точность: "))
e = 1
i = 1
a = 1
while a >= x:
    a = 1 / math.factorial(i)
    e += a
    i += 1
print(f"e = {e}") """

""" n = int(input("Введите кол-во элементов: "))
l = []
for i in range(n):
    l.append(int(input(f"Введите {i+1} элемент: ")))
for i in range(n):
    for j in range(len(l)-1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(l)

x = int(input("Введите элемент для поиска: "))
left = 0
right = len(l) - 1
found = False
while left <= right:
    mid = (left + right) // 2
    if l[mid] == x:
        print(f"Элемент {x} найден, позиция: {mid + 1}")
        found = True
        break
    elif l[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
if found == False:
    print("Элемент не найден") """

""" x = int(input("Введите натуральное число: "))
divisors = []
for i in range(1, x):
    if x % i == 0:
        divisors.append(i)
if sum(divisors) == x:
    print("Число совершенное")
else:
    print("Число несовершенное") """

n = int(input("Введите N: "))
s = 0
for i in range(1, n + 1):
    s += 1 / i
print(f"Сумма ряда = {s}")
