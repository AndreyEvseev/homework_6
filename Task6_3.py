# Задание 3. Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

numbers_list = [1, 2, 3, 5, 1, 5, 3, 10]
result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
print(f'Для последовательности {numbers_list} список уникальных элементов => {result_list}')
