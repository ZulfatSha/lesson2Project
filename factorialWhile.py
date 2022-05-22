#Задача 4. Найти произведение ряда чисел от 1 до 10

n = int(input('Введите число для вычисления его факториала: '))

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)