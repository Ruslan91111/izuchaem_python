import asyncio
import datetime
import random


async def my_sleep_func():
    await asyncio.sleep(random.randint(0, 5))


# Асинхронная функция display_date,
# которая принимает число(в качестве идентификатора)
# и цикл обработки событий в качестве параметров.
async def display_date(num, loop):
    # Функция имеет бесконечный цикл, который прерывается через 50 секунд.
    end_time = loop.time() + 50.0

    while True:
        # Но за этот период, она неоднократно печатает время и делает паузу.
        print("Loop: {} Time {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        # Функция await может ожидать завершения выполнения других
        # асинхронных функций (корутин).
        await my_sleep_func()


loop = asyncio.get_event_loop()


# Передаем функцию в цикл обработки событий (используя метод ensure_future).
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

# Запускаем цикл событий.
loop.run_forever()


#Всякий раз, когда происходит вызов await, asyncio понимает,
# что функции, вероятно, потребуется некоторое время.
# Таким образом, он приостанавливает выполнение, начинает мониторинг
# любого связанного с ним события ввода-вывода и позволяет запускать задачи.
# Когда asyncio замечает, что приостановленный ввод-вывод функции готов,
# он возобновляет функцию.




