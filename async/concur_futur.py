from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(5)
    return message


pool = ThreadPoolExecutor(3)

future = pool.submit(return_after_5_secs, ("hello"))
print(future.done())
sleep(5)
print(future.done())
print(future.result())


# ThreadPoolExecutor и ProcessPoolExecutor.  
# Эти исполнители поддерживают пул потоков или процессов.
# Мы отправляем наши задачи в пул, и он запускает задачи в доступном потоке / процессе.
# Возвращается объект Future, который можно использовать для запроса и
# получения результата по завершении задачи.


