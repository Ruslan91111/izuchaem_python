#  iterable-класс
class Letters:
    def __init__(self, string):
        self.letters = []
        for i in string:
            self.letters.append(f'-{i}-')

    def __iter__(self):
        return LettersIterator(self.letters[:])


# и связанный с ним iterator-class
class LettersIterator:
    def __init__(self, letters):
        self.letters = letters

    def __iter__(self):
        return self

    def __next__(self):
        if not self.letters:
            raise StopIteration
        item = self.letters[0]
        del self.letters[0]
        return item


kit = Letters('aeoui')
print(kit.letters)

for i in kit:
    print(i)

print(kit.letters)

