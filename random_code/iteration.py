class InfiniteSquaring:
    """Класс обеспечивает бесконечное последовательное возведение
    в квадрат заданного числа."""
    def __init__(self, initial_number):
        # Здесь хранится промежуточное значение
        self.number_to_square = initial_number

    def __next__(self):
        # Здесь мы обновляем значение и возвращаем результат
        self.number_to_square = self.number_to_square ** 2
        return self.number_to_square

    def __iter__(self):
        """Этот метод позволяет при передаче объекта функции iter
        возвращать самого себя, тем самым в точности реализуя
        протокол итератора."""
        return self


squaring_of_six = InfiniteSquaring(6)
next(squaring_of_six)
next(squaring_of_six)


class A:
    def __init__(self, a):
        self.a = a

    def __next__(self):
        if self.a > 0:
            self.a -= 1
            return print(f'прошла 1 итерация класса A, осталось {self.a}')
        else:
            raise StopIteration


examp = A(5)
examp.__next__()
next(examp)

# Вызов next() работает, но если мы попробуем передать объект
# циклу for, получим ошибку.

examp2 = A(5)
try:
    for i in examp2:
        print(i)
except TypeError:
    print('examp2 нельзя передать в for \n'
          'объект типа А не является итерируемым объектом')


# Другими словами цикл for ожидает, что после in будет стоять
# итерируемый объект, а не итератор

# Цикл for ожидает, что у объекта есть не только метод __next__,
# но и __iter__, задача которого превращать итерируемый объект в
# итератор.


# Если в цикл for передается уже итератор, то метод __iter__()
# этого объекта должен возвращать сам объект


class B:
    def __init__(self, b):
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.b > 0:
            self.b -= 1
            return print(f'прошла 1 итерация класса B, осталось {self.b}')
        else:
            raise StopIteration


examp_B = B(5)
examp_B.__next__()
examp_B.__next__()
next(examp_B)
next(examp_B)
next(examp_B)

examp_B = B(5)
for i in examp_B:
    print(i)

print('Подправим класс А')
class A2(A):
    def __iter__(self):
        return self


examp_A_after = A2(5)
for i in examp_A_after:
    print(i)


