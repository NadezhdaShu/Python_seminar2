# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:
#- 6782 -> 23
#- 0,56 -> 11

number = str(input("введите число n: "))

result = 0

for i in number:
    if i.isdigit():
        result = result + int(i)

print(f"Сумма цифр в {number} = {result}")