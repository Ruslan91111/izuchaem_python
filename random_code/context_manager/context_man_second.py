

class ContManager(object):
    def __init__(self):
        print('__init__')

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, type, value, traceback):
        print('__exit__:', type, value)
        return True  # Подавить исключение

    def __del__(self):
        print('__del__', self)


with ContManager() as c:
    print('Делаем что-нибудь с с: ', c)
    raise RuntimeError()
print('Завершаем действия')

print('Выполнено')



