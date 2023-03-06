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
    # корутины асинхронных функций func1, func2 обернули в задачи task1, task2
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(4))

    # в асинхронной функции main обозначили точки переключения к задаче task1 и task2
    await task1
    await task2


print(time.strftime('%X'))
# корутину асинхронной функции main передали в функцию asyncio.run
asyncio.run(main())
print(time.strftime('%X'))


# Перед определениями функций появился префикс async. Он говорит интерпретатору,
# что функция должна выполняться асинхронно. Вместо привычного time.sleep
# мы использовали asyncio.sleep. Это "неблокирующий sleep".
# В рамках функции ведет себя так же, как традиционный, но не останавливает
# интерпретатор в целом. Перед вызовом асинхронных функций появился префикс await.
# Он говорит интерпретатору примерно следующее: "я тут возможно немного потуплю,
# но ты меня не жди — пусть выполняется другой код, а когда у меня будет
# настроение продолжиться, я тебе маякну".
#
# На базе функций мы при помощи asyncio.create_task создали задачи (что это такое разберем позже) и запустили все это при помощи asyncio.run

