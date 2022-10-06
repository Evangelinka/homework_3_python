# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
# Создаем список вещественных чисел от 1 до 10
n = int(input('Введите длину списка: '))
my_list_float_rand = []
for i in range(1, n+1):
    my_list_float_rand.append(round(random.uniform(1,10),2))
result_list = []
# Берем остатки всех чисел и складываем в новый лист
for i in my_list_float_rand:
    if i % 1 != 0:
        result_list.append(round(i % 1, 2))
# Ищем минимальный и максимальный остаток и находим разницу
max_float = result_list[0]
min_float = result_list[0]
for i in result_list:
    if i > max_float:
        max_float = i
    elif i < min_float:
        min_float = i
print('Исходный список: ', my_list_float_rand)
print('Список без целой части: ', result_list)
print('Минимальное значение ', min_float)
print('Mаксимальное значение ', max_float)
print('Разница : ', round(max_float-min_float,2))