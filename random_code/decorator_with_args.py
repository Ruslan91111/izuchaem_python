# Чтобы получить декоратор, в который можно передать аргументы,
# нужно из функции с параметрами вернуть функциональный объект,
# который может действовать как декоратор.

# Декоратор @repeater() будет повторять декорируемую функцию,
# переданное в качестве аргумента, количество раз.
import functools


def repeater(repeat=1):
    """Повторение выполнение кода"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(repeat):
                print(f'{i+1}: ', end='')
                val = func(*args, **kwargs)
            return val
        return wrapper
    return decorator

# Функция repeater, которая принимает аргументы,
# возвращает ссылку на функцию декоратор().

# В простых декораторах без передачи агрументов используется
# @decorator без круглых скобок.
# Чтобы передавать в круглые скобки агументы, декоратор нужно
# обернуть в другую функцию, которая бы возвращала наш декоратор
# @repeater(repeat=3)
# Аргумент repeat, явно не используется в самой функции repeater(),
# но при передаче параметра создается замыкание, где repeat сохраняется
# до тех пор, пока оно не будет использовано позже функцией wrapper()

@repeater(repeat=4)
def say(name):
    print(f'Hello {name}')

say('Ruslan')


import time


def delayed(delay=1.5):
    "Задержка перед вызовом функции"
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Спим {delay} сек.')
            time.sleep(delay)
            val = func(*args, **kwargs)
            return val
        return wrapper
    return decorator


@delayed(delay=1)
def countdown(int_num):
    if int_num < 1:
        exit(0)
    else:
        print(int_num)
    countdown(int_num - 1)


countdown(4)




