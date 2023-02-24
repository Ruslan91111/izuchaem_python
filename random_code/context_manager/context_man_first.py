# Три самостоятельных функции, имитирующие:
# установление соединения
def setup():
    pass


# работу в файле
def do_work():
    pass


# разрыв соединения после работы
def teardown():
    pass


# Имитация работы с объектом.
# Python код с общей настройкой и завершением, то есть с использованием
# описанных выше функций.
setup()
try:
    do_work()
finally:
    teardown()


# Теперь работа с помощью контекстного менеджера.

# Собственный контекст менеджер.
class ContextManager(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        # данный метод обязательно возвращает сам объект
        return self.file_obj

    def __exit__(self, type, value, traceback):
        # отлавливает исключения и закрывает соединения
        self.file_obj.close()


# Имитация работы с объектом при помощи созданного выше ContextManager.

# Создали объект класса контекст менеджера
cm = ContextManager()
# вошли в него
obj = cm.__enter__()
try:
    # передали функции объект контекст менеджера
    do_work(obj)
finally:
    # вышли
    cm.__exit__()


# Лаконичная форма с помощью оператора 'with':
with ContextManager() as obj:
    do_work()

# Простые менеджеры контекста также могут быть написаны
# с использованием генераторов и декоратора contextmanager:

