"""
Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no

"""

number = int(input("Введите билет: "))
first_past = number // 1000
first_sum = first_past % 10 + (first_past // 10) % 10 + first_past // 100

second_past = number % 1000
second_sum = second_past % 10 + (second_past // 10) % 10 + second_past // 100

print("yes") if first_sum == second_sum else print("no")
