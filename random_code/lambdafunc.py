from functools import reduce

double = lambda x: x * 2
print(double(10))

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]

# Использование функции filter() для отбора четных чисел из списка.
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

# Использование функции map() для удвоения всех элементов списка.
new_list2 = list(map(lambda x: (x * 2), my_list))
print(new_list2)

# Использование функции reduce().
new_list3 = reduce((lambda x, y: x + y), my_list)
print(new_list3)

# Лямбда и  списковое включение.
new_list4 = [lambda x=x: x ** 2 for x in range(1, 10)]
for i in new_list4:
    print(i())

# Определить какая из двух цифр больше.
max_num = lambda a, b: a if a > b else b
print(max_num(3, 5))

list_of_lists = [[10, 6, 9], [0, 14, 16, 80], [8, 12, 30, 44]]

# Отсортирует каждый список в общем списке.
sorted_list = lambda x: (sorted(i) for i in x)

# Принимает список и функцию.
# Функция возвращает второй элемент с конца каждого списка, перебираемого в цикле for.
# y - это условно список.
second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]

# Вызываем через переменную lambda функцию, куда передаем список и другую нашу lambda функцию.
result = second_largest(list_of_lists, sorted_list)
print(result)



