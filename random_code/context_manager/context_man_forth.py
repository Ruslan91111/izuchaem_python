# В стандартную библиотеку Python входит модуль contextlib,
# который содержит утилиты для построения и работы
# с контекстными менеджерами.

# В данном модуле рассмотривается инструмент  – contextmanager.
# contextmanager используется как декоратор для функции,
# превращая ее в контекстный менеджер.
# При этом схема конструирования
# такая: все, что написано до оператора yield вызывается в рамках
# функции __enter__, а все что после – в рамках __exit__.


from contextlib import contextmanager


@contextmanager
def processor():
    print('-->Start processing')
    yield
    print('<-- stop processing')


with processor():
    print(':: processing')


# В contextmanager можно завернуть работу с файлом.

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    yield f
    f.close()


with open_file('test.txt', 'w') as fw:
    fw.write('hello')



