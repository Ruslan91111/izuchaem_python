"""Пример асинхронной функции, но без задач,
 пример с задачами в cooking_with_asyncio.py"""
import asyncio


async def waiter() -> None:
    await cook('Паста', 8)
    await cook('Салат Цезарь', 3)
    await cook('Отбивные', 16)


async def cook(order, time_to_prepare) -> None:
    print(f'Новый заказ: {order}')
    await asyncio.sleep(time_to_prepare)
    print(order, ' - готово')


# По сути, run берет низкоуровневый псевдо-сервер asyncio,
# который называется рабочим циклом. Этот цикл является
# координатором, который следит за приостановкой и возобновлением
# задач из кода.
asyncio.run(waiter())

