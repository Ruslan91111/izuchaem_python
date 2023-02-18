
# объемлющая функция
def print_msg(msg):
    # вложенная функция
    def printer():
        print(msg)
    printer()


print_msg("Hello")
# Output: Hello


def print_msg2(msg):

    def printer():
        print(msg)

    # Возвращает вложенную функцию.
    return printer


another = print_msg2("Hello")
another()
print(type(another))
print(another)

# Output: Hello

# Функция print_msg2() вызывалась со строкой «Hello»,
# а возвращаемая функция была присвоена переменной another.
# При вызове another() сообщение все еще сохранялось в памяти,
# хотя мы уже закончили выполнение функции print_msg().
# Этот метод, с помощью которого некоторые данные (в данном случае строка «Hello»)
# прикрепляются к некоторому коду, в Python называется замыканием.
# Ссылка на переменную объемлющей функции действительна, даже когда объемлющая функция
# закончила работу, и переменная вышла из области видимости или сама функция
# удаляется из текущего пространства имен.

del print_msg2
print('call - another()')
another()
try:
    print_msg2('Hi')
except NameError:
    print('func print_msg2 deleted')


# Another example of closure.

def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


times3 = make_multiplier_of(3)
# 3 присваивается переменной внешней функции - объемлющей.


times5 = make_multiplier_of(5)
# 5 присваивается переменной внешней функции - объемлющей.


print(times3(4))
# аргумент 4 передается в x
# n = 3
# x = 4


print(times5(7))
# n = 5
# x = 7


print(times3(times5(2)))
# n = 5
# x = 2
# n = 3
# x = 10

print(make_multiplier_of.__closure__)
print(times3.__closure__)
print(times3.__closure__[0].cell_contents)


print('last_example')
def clos_func(arg1, arg2):
    def inner_func(arg3, arg4):
        print((arg1+arg2) * (arg3+arg4))

    return inner_func


x1 = clos_func(3, 4)

del clos_func

x2 = x1(5, 6)

print(x2)






