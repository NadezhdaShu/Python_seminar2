# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции задаются с клавиатуры через пробел.

N = int(input("Введите число N: "))

if N < 0:
    N *= -1
list_of_numbers = []

import random

for i in range(-N, N+1):
    list_of_numbers.append(random.randint(-N, N))

print(list_of_numbers)
 
pos1 = int(input("Введите позицию 1: "))
pos2 = int(input("Введите позицию 2: "))

proiz = 1
proiz = list_of_numbers[pos1] * list_of_numbers[pos2]

print(f"Произведения элементов: {proiz}")