# Декоратор с аналогичным функционалом, но реализованный через класс.
import functools
import time


class DelayedCls:
    # запоминаем аргументы декоратора
    def __init__(self, delay=1):
        self._delay = delay

    # декоратор общего назначения
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Спим {self._delay} сек.')
            time.sleep(self._delay)
            val = func(*args, **kwargs)
            return val

        return wrapper


@DelayedCls(delay=2)
def countdown2(int_num):
    if int_num < 1:
        exit(0)
    else:
        print(int_num)
    countdown2(int_num - 1)


countdown2(4)
