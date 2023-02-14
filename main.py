from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('doing something')
        res = func(*args, **kwargs)
        print('doing something after')
        return res
    return wrapper


@decorator
def som():
    print('a' * 3 + '!')
print(som)

