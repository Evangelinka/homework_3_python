# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
n = int(input('Введите длину списка: '))
my_list_rand = []
for i in range(1, n+1):
    my_list_rand.append(random.randint(1, 9))
sum_odd = 0
for i in range(1, len(my_list_rand), 2):
    sum_odd += my_list_rand[i]
print(
    f'Массив: {my_list_rand}, сумма элементов на нечетных позициях: {sum_odd}')