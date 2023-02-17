""" Класс хеширования. Два метода: размещение и поиск значения. """
class HashTable:
    def __init__(self):
        # размер хэш-таблицы
        self.size = 11
        # ключи
        self.slots = [None] * self.size
        # значения
        self.data = [None] * self.size

    def put(self, key, data):
        # Хэш-значение, вычисленное ХЭШ функцией.
        hashvalue = self.hashfunction(key, len(self.slots))

        # если слот под этим Хэшем не занят, то сохранить его ключ и значение
        # С доступом по ключу и там и там.
        if not self.slots[hashvalue]:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        # Если слот не пустой
        else:
            # Если в этом слоте тот же ключ. Заменить значение.
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            # Иначе смотреть следующие слоты по одному, пока не найдем пустой слот.
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while not self.slots[nextslot] and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                # Выход из цикла. Если пустой слот будет найден.
                # Присвоить значения ключу и значению.
                if not self.slots[nextslot]:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                # Если ключ есть, то заменить значение.
                else:
                    self.data[nextslot] = data

    # Метод высчитывающий хеш.
    def hashfunction(self, key, size):
        return key % size

    # Метод для поиска следующего слота.
    def rehash(self, olhash, size):
        return (olhash +1) % size

    # Перегружаем метод get.
    def get(self, key):
        # Высчитываем хеш.
        startslot = self.hashfunction(key, len(self.slots))

        # Флаги для поиска
        data = None
        stop = False
        found = False
        position = startslot

        while not self.slots[position] \
                and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)







