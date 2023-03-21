"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
from random import randint

n = int(input("Введите количество монеток "))
coins = []

for i in range(n):
    coins.append(randint(0, 1))

head = 0    #орёл
tail = 0    #решка

for i in coins:
    if i == 1:
        head = head + 1
    else:
        tail = tail + 1

print(f"head {head}")
print(f"tail {tail}")

if head <= tail:
    print(head)
else:
    print(tail)
