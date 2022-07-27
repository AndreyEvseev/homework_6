# Задание 2_1. Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

import random

n = int(input('Количество элементов списка: '))
b1 = int(input('Граница 1 диапазона значений элементов списка: '))
b2 = int(input('Граница 2 диапазона значений элементов списка: '))
numbers_list = [random.randint(min(b1, b2), max(b1, b2)) for i in range(n)]
result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
print(f'Для последовательности {numbers_list}, \n   список уникальных элементов => {result_list}')
