from multiprocessing import Pool


def f(x):
    return x * x


# С помощью класса Pool мы также можем распределить выполнение одной функции
# между несколькими процессами для разных входных значений
if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))

# Здесь вместо того, чтобы перебирать список значений и вызывать функцию f по одному,
# мы фактически запускаем функцию в разных процессах.
# Один процесс выполняет f(1), другой-f(2), а другой-f (3).
# Наконец, результаты снова объединяются в список.
# Это позволяет нам разбить тяжелые вычисления на более мелкие части и
# запускать их параллельно для более быстрого расчета.

