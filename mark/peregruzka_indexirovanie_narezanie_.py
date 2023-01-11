class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]


class Indexer2:
    def __getitem__(self, index):
        if isinstance(index, int): #проверка режима использования
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

