# Пример со счетчиком, сделать атрибут __count приватным, чтобы отслеживать создание
# и удаление экземпляров класса
class B:
    __count = 0

    def __init__(self):
        B.__count += 1

    def __del__(self):
        B.__count -= 1


a = B()
try:
    print(B.__count)
except AttributeError:
    print('Это приватный атрибут')

print('-'*25)
print('Но доступ к атрибуту все равно имеется через: {B._B__count} \n или {a._B__count}')
print()


# Защитили поле от случайных изменений. Теперь добавим метод, чтобы получить его значение.

class C:
    __count = 0

    def __init__(self):
        C.__count += 1

    def __del__(self):
        C.__count -= 1

    # Метод qty_object() не принимает объект (нет self'а),
    # поэтому вызывать его надо через класс.
    def qty_objects():
        return C.__count

c1 = C()
c2 = C()
print('-'*25)
print('Общее количество экземпляров класса C: ', C.qty_objects())
print('-'*25)


# Методы также делаются приватными при помощи '__'
class DoubleList:
    def __init__(self, l):
        self.double = DoubleList.__make_double(l)  # Присваиваем атрибут экземпляру класса предварительно
                                                   # применив метод класса.

    def __make_double(old):
        new = []
        for i in old:
            new.append(i)
            new.append(i)
        return new


nums = DoubleList([1,2,3,4])
print('Создали экземпляр класса DoubleList', nums)
print('-'*25)
print('Обращаемся к атрибуту экземпляра nums - double: ', nums.double)
print('-'*25)

try:
    print(DoubleList.__make_double([1,2]))
except AttributeError:
    print('ОШИБКА. Приватный метод.')

print('-'*25)


# Ошибочное мнение, что скрытые поля при присваивании
# им значений становятся открытыми.

class D:
    def __init__(self, field):
        self.__field = field

    def set_field(self, field):
        self.__field = field

    def get_field(self):
        return self.__field

# Создаем экземпляр и передаем 8.
d1 = D(8)
print('Создаем экземпляр и передаем 8 ', d1.__dict__)

# Вызываем метод set_field и передаем 3.
d1.set_field(3)
print('Создаем экземпляр и передаем 3 ', d1.__dict__)

print('Вызываем метод get_field - ', d1.get_field())


# Выброс исключения, так как происходит обращение к еще несуществующему полю,
# а не потому, что это поле скрыто. Когда же этому полю присваивается
# значение 5, то у объекта появляется новое поле.
try:
    print(d1.__field)
except AttributeError:
    print('Пытаемся вывести на печать атрибут __field, но его нет.')

d1.__field = 5
print(d1.__field)
print(d1.__dict__)
print('d1.__field is d1._D__field - ответ: ', d1.__field is d1._D__field)


# В Python атрибуты объекту можно назначать за пределами класса.
class E:
    def __init__(self, value):
        self.field1 = value


e = E(10)

# Присваиваем объекту атрибут, который не был определен в классе.
# Создание атрибута проходит успешно.
e.field2 = 20
print('-'*25)

print('e.field1', e.field1)
print('e.field2', e.field2)


# Пресечь такое поведение можно с помощью метода
# перегрузки оператора присваивания атрибуту __setattr__():
class E2:
    def __init__(self, value):
        self.field1 = value

    def __setattr__(self, attr, value):
        if attr == 'field1':
            self.__dict__[attr] = value
        else:
            raise AttributeError


# Если внутренние атрибуты содержат скрытые поля.
# То следующий код приведет к исключению.
# class A:
#     def __init__(self, x):
#         self.__x = x
#
#     def __setattr__(self, attr, value):
#         if attr == "__x":
#             self.__dict__[attr] = value
#         else:
#             raise AttributeError
#
#
# a = A(5)

class F:
    def __init__(self, x):
        self.__x = x

    def __setattr__(self, attr, value):
        if attr == "_F__x":
            self.__dict__[attr] = value
        else:
            raise AttributeError



