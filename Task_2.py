# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
n = int(input('Введите длину списка: '))
my_list_rand = []
for i in range(1, n+1):
    my_list_rand.append(random.randint(1, 9))
print(my_list_rand)
my_prod = 0 
my_list_prod_pair = []
for i in range(0, len(my_list_rand)//2):
    my_prod = my_list_rand[i] * my_list_rand[-i-1]
    my_list_prod_pair.append(my_prod)
print(f'Исходный массив: {my_list_rand}, произведение пар чисел: {my_list_prod_pair}')