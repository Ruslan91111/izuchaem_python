from functools import wraps


def decorator(func):
    @wraps(func)     # Придает сигнатуру функции.
    def wrapper(*args, **kwargs):
        print('doing something')
        res = func(*args, **kwargs)
        print('doing something after')
        return res
    return wrapper   # Возвращает функцию без вызова.


@decorator     # Синтаксический сахар.
def som():
    print('a' * 3 + '!')

print(som)  # <function som at 0x7f5593ad8940>

print(som)  # Без wraps в декораторе.
            # <function decorator.<locals>.wrapper at 0x7fe42b038940>

# Вызвать функцию, украшенную декоратором.
som()
print("it's was first")

som2 = decorator(som)
som2()
print("it's was second")

# Пробросить аргумент.
def outer(a=1):     # Обернули в еще одну функцию.
    def decorator(func):
        @wraps(func)     # Придает сигнатуру функции.
        def wrapper(*args, **kwargs):
            print('doing something')
            res = func(*args, **kwargs)
            print('doing something after')
            return res
        return wrapper   # Возвращает функцию без вызова.
    return decorator     # Вернули функцию.


@outer(123)   # Синтаксический сахар, в который уже можно передавать аргументы.
def som():
    print('a' * 3 + '!')

som()
print("it's was third")

