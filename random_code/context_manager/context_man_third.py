# Класс, с методом post_work(), вызываемым
# перед прекращением работы с ним.
class Resource:
    def __init__(self, name):
        print('Resource: create {}'.format(name))
        self.__name = name

    def get_name(self):
        return self.__name

    def post_work(self):
        print('Resource: close')


# Создаем контекстный менеджер для работы с Resource,
# который можно будет использовать с оператором with.

class ResourceForWith:
    def __init__(self, name):
        self.__resource = Resource(name)

    def __enter__(self):
        return self.__resource

    def __exit__(self, type, value, traceback):
        self.__resource.post_work()


# Пример работы с ResourceForWith и конструкцией with.
with ResourceForWith('Worker') as r:
    print(r.get_name())





