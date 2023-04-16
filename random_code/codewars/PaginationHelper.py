"""Помощник в пагинации. Помогает определить сколько эелементов в коллекции,
сколько элементов на определнной страницу, на какой странице определенный элемент"""
from math import ceil, floor


class PaginationHelper:
    # Инициализировать экземпляр, передать коллекцию, количество элементов на странице
    def __init__(self, collection, items_per_page):
        self._collection = collection
        self._items_per_page = items_per_page

    # Возвращает число элементов во всей коллекции
    def item_count(self):
        return len(self._collection)

    # Возвращает общее количество страниц.
    def page_count(self):
        return ceil(len(self._collection) / self._items_per_page)

    # Возвращает количество элементов на переданной странице. Начальная страница(первая) 0, -1 для страниц вне диапазона
    def page_item_count(self, page_index):
        # Для любой полной страницы.
        if (page_index + 1) * self._items_per_page <= self.item_count():
            return self._items_per_page
        # Для последней страницы.
        if page_index * self._items_per_page < self.item_count() < (page_index + 1) * self._items_per_page:
            return self.item_count() % self._items_per_page
        # В остальных случаях - вне диапазона.
        return -1

    # Определяет на какой странице расположен элемент. -1 для элементов вне диапазона.
    def page_index(self, item_index):
        if 0 <= item_index < self.item_count():
            return floor(item_index/ self._items_per_page)
        else:
            return -1


helper = PaginationHelper(['a','b','c','d','e','f'], 4)

print(helper.page_index(5))
print(helper.page_index(2))
print(helper.page_index(20))
