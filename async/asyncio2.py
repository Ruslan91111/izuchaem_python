import time
import asyncio


# Пример работы в синхронном режиме.
# Быстрая операция - арифметическая, медленная - вывода.
def func1(x):
    print(x ** 2)
    time.sleep(3)
    print('func1 завершена')


def func2(x):
    print(x ** 0.5)
    time.sleep(3)
    print('func2 завершена')


def main():
    func1(4)
    func2(4)


# print(time.strftime('%X'))
# main()
# print(time.strftime('%X'))

# Обе функции будут выполнены за 6 секунда, 3 секунды на каждую.
# func2 ждет пока отработает func1 и только потом начинает
# выполнять работу.


# Пример работы в асинхронном режиме.
async def func_async1(x):
    print(x**2)
    await asyncio.sleep(3)
    print("func_async1 завершена")


async def func_async2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('func_async2 завершена')


async def main():
    task1 = asyncio.create_task(func_async1(4))
    task2 = asyncio.create_task(func_async2(4))

    await task1
    await task2


print(time.strftime('%X'))
asyncio.run(main())
print(time.strftime('%X'))

# Выполнение двух функций происходит в асинхронном режиме
# и укладывается в 3 секунды.
# Сделали фукнции асинхронными, обернули в задачи - tasks.
# Установили await - точки переключения.


print(type(func1))
print(type(func1(4)))
# <class 'function'>
# 16
# func1 завершена
# <class 'NoneType'>

#
# print(type(func_async1))
# print(type(func_async1(4)))








