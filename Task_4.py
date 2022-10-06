# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('Введите десятичное число: '))
str_remainder = ''
while n > 0:
    str_remainder = str(n % 2) + str_remainder
    n //= 2
print(str_remainder)