# Класс объект поэтому его можно возвращать.
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


MyClass = choose_class('foo')
print(MyClass)     # функция возвращает класс, а не экземпляр
                   # <class '__main__.choose_class.<locals>.Foo'>
print(MyClass())   # можно создать экземпляр этого класса
                   # <__main__.choose_class.<locals>.Foo object at 0x7efd016af250>


# return type of object
print(type(1))
print(type('ruslan'))


# С помощью type можно создавать классы.
# type(<имя класса>,
#        <кортеж родительских классов>, # для наследования, может быть пустым
#        <словарь, содержащий атрибуты и их значения>)
MyNewClass = type('MyNewClass', (), {})
print(MyNewClass)
print(MyNewClass())


# Создание класса с помощью type
Foo = type('Foo', (), {'bar': True, 'name': 'ruslan'})


def echo_bar(self):
    print(self.bar)


#  Присвоить функию в качестве метода.
FooChild = type('FooChild', (Foo, ), {'echo_bar': echo_bar})
a = FooChild()
a.echo_bar()


# Код, чтобы все создаваемые классы были в верхнем регистре.
def upper_attr(future_class_name,  future_class_parents,
               future_class_attr):
    """
      Возвращает объект-класс, имена атрибутов которого
      переведены в верхний регистр
    """
    # берём любой атрибут, не начинающийся с '__'
    attrs = ((name, value) for name, value in future_class_attr.items()
             if not name.startwith('__'))

    # переводим их в верхний регистр
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # создаём класс с помощью `type`
    return type(future_class_name, future_class_parents, uppercase_attr)


# Это сработает для всех классов в модуле.
# Определяем метакласс на уровне модуля.
__metaclass__ = upper_attr


class Foo(object):
  # или можно определить __metaclass__ здесь, чтобы сработало только для этого класса
  bar = 'bip'

print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True

f = Foo()










