"""Пример синхронной функции
асинхронный пример в  cooking_with_asyncio.py"""

import time


def waiter():
    cook('Паста', 8)
    cook('Салат Цезарь', 3)
    cook('Отбивные', 16)


def cook(order, time_to_prepare):
    print(f'Новый заказ: {order}')
    time.sleep(time_to_prepare)
    print(order, ' - готово')


if __name__ == '__main__':
    waiter()




