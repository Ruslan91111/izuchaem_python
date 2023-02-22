import asyncio
import time


async def func1(x):
    print(x**2)
    await asyncio.sleep(3)
    print("func1 завершена")


async def func2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('func2 завершена')


# Асинхронная функция main
async def main():
    # корутину асинхронной функции func1 обернули задачей task1
    task1 = asyncio.create_task(func1(4))
    # корутину асинхронной функции func2 обернули задачей task1
    task2 = asyncio.create_task(func2(4))
    # в асинхронной функции main обозначили точку переключения к задаче task1
    await task1
    # в асинхронной функции main обозначили точку переключения к задаче task2
    await task2


print(time.strftime('%X'))
# корутину асинхронной функции main передали в функцию asyncio.run
asyncio.run(main())
print(time.strftime('%X'))




