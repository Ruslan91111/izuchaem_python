from random import randint

a = [1, 2, 3]

# списковое включение
b = [i ** 2 for i in a]

print(a)
print('Применено списковое включение - ', b)

# Чтобы изменить первоначальный список.
a = [i ** 2 for i in a]
print(a)

#  Альтернатива верхнему коду.
for index, value in enumerate(a):
    a[index] = value ** 2

print('альтернатива списковому включению - ', a)


nums = [randint(10, 20) for i in range(10)]
print(nums)

nums = [i for i in nums if i % 2 == 0]
print('Поставили услвоие для четных - ', nums)

# Генераторы списков могут содержать вложенные циклы.
a = "Aa"
b = "Bb"
c = "Cc"

encl_for = [i + j + k for i in a for j in b for k in c]
print('Результат с вложенными циклами for ', encl_for)


# Аналогичные включения словарей и множеств.
dict_compr = {i : i + 10 for i in range(11, 15)}
print(dict_compr)

set_compr = {i for i in range(11, 15)}
print(set_compr)

# Генераторы
generat = (i for i in range(2, 8))
print(type(generat))

for i in generat:
    print(i)

# Второй раз не пробежишься, так как объект-генератор уже сгенерировал
# все значения по заложенной в него "формуле".
for i in generat:
    print(i)


# Генератор через функцию.
def func_gen(start, finish):
    while start < finish:
        yield start * 0.33
        start += 1


x = func_gen(1, 5)
print('Так можно вызвать следующий объект - x.__next__() ', x.__next__())
print('И следующий объект вызвать также через - x.__next__() ', x.__next__())

# Тот же генератор через выражение
b = (i * 0.33 for i in range(1, 5))
print(b.__next__())

print('Цикл for продолжит выдавать значение со второго значения.')

# Цикл for продолжит выдавать значение со второго значения.
for i in b:
    print(i)

