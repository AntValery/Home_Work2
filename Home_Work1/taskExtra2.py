"""
Задача 2: Найдите сумму цифр трехзначного числа.

 *Пример:*

 123 -> 6 (1 + 2 + 3)
 100 -> 1 (1 + 0 + 0)
"""

number = int(input("Введите трёхзначное число = "))

first = int(number / 100)
second = int((number / 10) % 10)
third = int(number % 10)

print(first + second + third)

