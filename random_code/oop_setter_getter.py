# Пример с геттером и сеттером
class A:
    def __init__(self, a):
        self.__a = a  # Приватный атрибут

    # Два безопасных метода, чтобы обратиться к приватному атрибуту или изменить его значение.
    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a


x = A(1)
print(x.get_a())

x.set_a(5)
print(x.get_a())


# Пример со свойством - функцией property().
class B:
    def __init__(self, b):
        self.__b = b  # Приватный атрибут

    def get_b(self):
        return self.__b

    def set_b(self, w):
        self.__b = w

    def del_b(self):
        del self.__b

    b = property(get_b, set_b, del_b)


xb = B(1)
print(xb.b)

xb.b = 55
print(xb.b)


# декоратор property
class C:
    def __init__(self, b):
        self.__b = b  # Приватный атрибут


    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, w):
        self.__b = w + 11

    @b.deleter
    def del_b(self):
        del self.__b


print('C-class')
xc = C(1)
print(xc.b)

xc.b = 55
print(xc.b)

# del (xc)
print(xc.b)


class ClassWithProperties:
    def __init__(self):
        self.someAttribute = 'some initial value'
    @property
    def someAttribute(self): # Get-метод
        return self.__someAttribute
    @someAttribute.setter
    def someAttribute(self, value): # Set-метод
        self.__someAttribute = value
    @someAttribute.deleter
    def someAttribute(self): # Del-метод
        del self.__someAttribute

obj = ClassWithProperties()
print(obj.someAttribute) # Выводит 'some initial value'
obj.someAttribute = 'changed value'
print(obj.someAttribute) # Выводит 'changed value'
# print(obj._ClassWithProperties__someAttribute)
del obj.someAttribute # Удаляет атрибут _someAttribute.
