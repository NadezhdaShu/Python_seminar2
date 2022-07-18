#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input("Введите число N: "))

def Factorial(n):
    result = 1

    for i in range(n):
        result *= i + 1

    return result

result_array = [0] * n

for i in range(n):
    result_array[i] = Factorial(i + 1)

print(f"Произведения чисел: {result_array}")