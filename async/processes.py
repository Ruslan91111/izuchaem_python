"""Работа процессов"""
import multiprocessing
import time
import random


# Функция worker будет выполняться в нескольких процессах асинхронно и одновременно.
# Функция ничего не делает только запускается на какой-то период времени.
def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print(f"I am Worker № {number}, I slept for {sleep} seconds")


for i in range(5):
    t = multiprocessing.Process(target=worker, args=(i,))
    t.start()


print("All Processes are queued, let's see when they finish!")
# I am Worker № 2, I slept for 3 seconds
# I am Worker № 4, I slept for 6 seconds
# I am Worker № 3, I slept for 8 seconds
# I am Worker № 1, I slept for 8 seconds
# I am Worker № 0, I slept for 9 seconds

# Таким образом мы запустили 5 процессов для совместной работы и после их старта
# (т.е. после запуска функции worker) операция не ждёт завершения работы процессов
# прежде чем перейти к следующему оператору print. Это асинхронная операция.

# Отличие от потоков (threads).Теперь вместо множества потоков мы используем
# процессы, которые запускаются на разных ядрах CPU.









