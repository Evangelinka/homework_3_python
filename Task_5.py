# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))
list_fibonacci_nega = []
b1 = 0
b2 = 1
for i in range(n):
    b1, b2 = b2, b1 - b2
    list_fibonacci_nega.append(b1)
list_fibonacci_nega = list_fibonacci_nega[::-1]
list_fibonacci_nega.append(0)
a1 = 0
a2 = 1
list_fibonacci = []
for i in range(n):
    a1, a2 = a2, a1 + a2
    list_fibonacci.append(a1)
result = list_fibonacci_nega + list_fibonacci
print(result)