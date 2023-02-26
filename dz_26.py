# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии. *Пример:* A = 3; B = 5 -> 243 (3⁵) A = 2; B = 3 -> 8

def degree(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    return x * degree(x, y - 1)


number_a = int(input('A= '))
number_b = int(input('B= '))
print(degree(number_a, number_b))
