"""
total (spam, 1, 2, а=3, b=4, _reps=1000) вызывает и хронометрирует spam(l, 2, а-3, Ь=4)
_reps раз и возвращает суммарное время для всех прогонов с финальным результатом.
bestof(spam, 1, 2, а=3, b=4, _reps=5) запускает тест лучшего из N в попытке
избавиться от влияния колебаний загрузки системы и возвращает лучшее время
среди _reps тестов.
bestoftotal(spam, 1,  2, а=3, b=4, _repsl=5, _reps=1000) запускает тест
лучшего суммарного времени, который берет лучший из _repsl прогонов
(суммарного времени _reps прогонов);
"""
import time, sys

timer = time.perf_counter if sys.platform[:3] == 'win' else time.time()

def total(func, *args, **kwargs):
    _reps = kwargs.pop('_reps', 1000) #переданное или стандартное количество повторений
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *args, **kwargs):
    _reps =kwargs.pop('_reps', 5)
    best = 2**32
    for i in range(_reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)

def bestoftotal(func, *args, **kwargs):
    _reps1 = kwargs.pop('_reps1', 5)
    return min(total(func, *args, **kwargs) for i in range(_reps1))


