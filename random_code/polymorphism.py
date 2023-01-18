# Демонстрация классического метода __str__
class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2


a = A(3, 4)
b = str(a)

# print() вызывает str()
print(a)
print(b)
# Вывод: <__main__.A object at 0x000001F243B75390>
#        <__main__.A object at 0x000001F243B75390>

# Если нужно, чтобы, когда объект передается функции print(),
# выводилась какая-нибудь другая более полезная информация,
# то в класс надо добавить специальный метод __str__().
# Этот метод должен обязательно возвращать строку,
# которую будет в свою очередь возвращать функция str(),
# вызываемая функций print():


class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2

    def __str__(self):
        s = str(self.field1)+" "+str(self.field2)
        return s


a = A(3, 4)
b = str(a)
print(a)
print(b)


class Rectangle:
    def __init__(self, width, height, sign):
        self.w = int(width)
        self.h = int(height)
        self.s = str(sign)

    def __str__(self):
        rect = []
        for i in range(self.h):
            rect.append(self.s * self.w)

        rect = '\n'.join(rect)
        return rect


b = Rectangle(4, 5, '=')
print(b)


# Перегрузки операторов

class A:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return str(self.arg)


# Класс-агрегат B, содержащий в списке объекты класса А.
# Класс B принимает при создании экземпляра атрибуты неименованные
# после чего конструктор создавая объект, создает атрибут aList - пустой список,
# наполняет его через цикл for, по сути создавая объект класса A, передавая ему
# аргументы из arg
# A(i)
class B:
    def __init__(self, *args):
        self.aList = []
        for i in args:
            self.aList.append(A(i))


group = B(5, 10, 'abc')
print(group.aList[1])


class C:
    def __init__(self, *args):
        self.aList = []
        for i in args:
            self.aList.append(A(i))

# Извлекать элементы по индексу из самого объекта, а не из его поля.
# Метод __getitem__() перегружает операцию извлечения элемента по индексу.
# Метод вызывается, когда к объекту применяется операция извлечения элемента:
# объект[индекс].
    def __getitem__(self, i):
        return self.aList[i]


group = C(5, 10, 'abc')
print(group[1])


# Переопределить оператор вызова.
# __call__()
class Changeable:
    def __init__(self, color):
        self.color = color

    def __call__(self, newcolor):
        self.color = newcolor

    def __str__(self):
        return "%s" % self.color


canvas = Changeable("green")
frame = Changeable("blue")

canvas("red")
frame("yellow")

print(canvas, frame)

