import time
import asyncio


# Пример работы в синхронном режиме.


# Быстрая операция - арифметическая и медленная вывода.
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
# 09:40:58
# 16
# func1 завершена
# 2.0
# func2 завершена
# 09:41:04


# func2 ждет пока отработает func1 и только потом начинает
# выполнять работу.


print('Теперь в асинхронном режиме')

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
# 09:56:07
# 16
# 2.0
# func_async1 завершена
# func_async2 завершена
# 09:56:10

# Все укладывается в 3 секунды.


print(type(func1))
print(type(func1(4)))
# <class 'function'>
# 16
# func1 завершена
# <class 'NoneType'>

#
# print(type(func_async1))
# print(type(func_async1(4)))








