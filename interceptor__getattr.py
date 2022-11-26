"""
Перехват функции getattr
образение только по атрибуту age
"""

class operators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)


# простая работа get и set свойств
class Properties:
    def getage(self):
       return 40

    def setage(self, value):
        print('set age: %s' % value)
        self._age = value
    age = property(getage, setage, None, None)

class operators2:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)
    def __setattr__(self, name, value):
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['age'] = value
        else:
            self.__dict__['name'] = value



