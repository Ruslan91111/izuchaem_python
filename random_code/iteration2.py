num_list = [1, 2, 3, 4, 5]


# Объекты, которые можно перебирать в цикле for содержат в себе объект-итератор
# Чтобы его получить, необходимо использовать функцию iter(),
# а для извлечения следующего элемента из итератора – функцию next().
itr = iter(num_list)
print(type(itr))
print('Первая итерация ', next(itr))
print('Вторая итерация ', itr.__next__())
print('Третья итерация ', next(itr))
print('Четвертая итерация ', next(itr))


class SimpleIterator:
    # Конструктор, принимающий количество единиц.
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

s_iter1 = SimpleIterator(5)
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))


# Функция, которая генерирует необходимое нам количество единиц.
def simple_generator(val):
    while val > 0:
        val -= 1
        yield 1

gen_iter = simple_generator(5)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
try:
    print(next(gen_iter))
except StopIteration:
    print('StopIteration')

