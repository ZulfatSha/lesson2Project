"""
serial_number = 0
number = '0000'
print(serial_number , number)
serial_number += 1
print(serial_number , number)
serial_number += 1
print(serial_number , number)
serial_number += 1
print(serial_number , number)
serial_number += 1
print(serial_number , number)
"""
#Задача 3: Вывести сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.

a = 1
b = 0
while a < 100+1:
    if a == 100:
        print(100, end='\n')
    else:
        print(a, end='+')
    b += a
    a = a + 1
print("Сумма ряда чисел равна:", b)
