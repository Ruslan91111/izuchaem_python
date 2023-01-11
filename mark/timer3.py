"""
Используется в точности как timer2.py, но для получения более простого кода
применяет аргументы с передачей только по ключевым словам и стандартными
значениями Python З.Х.
Выносить вызов range()  за пределы тестов в Python З.Х нет нужды, т.к. он
всегда дает генератор; данная версия не будет работать в Python 2.Х.
11  и и
"""

import time, sys

timer = time.perf_counter if sys.platform[:3] == 'win' else time.time()

def total(func, *args, _reps=1000,**kwargs):
    start = timer()
    for i in range(_reps):
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *args, _reps=5, **kwargs):
    best = 2**32
    for i in range(_reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)

def bestoftotal(func, *args, _reps=5, **kwargs):
    _reps1 = kwargs.pop('_reps1', 5)
    return min(total(func, *args, **kwargs) for i in range(_reps1))


