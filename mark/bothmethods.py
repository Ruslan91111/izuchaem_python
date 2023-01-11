class Methods:
    def imeth(self, x):    #нормальный метод: передается self
        print([self, x])

    def smeth(x):          # статический метод: экземпляр не передается
        print(x)

    def cmeth(cls, x):         #метод класса: получает класс, а не экземпляр
        print([cls, x])

    # Делает smeth статическим методов  (или 0:  впереди)
    smeth = staticmethod(smeth)
    # Делает cmeth методом класса  (или 0:  впереди)
    cmeth = classmethod(cmeth)


