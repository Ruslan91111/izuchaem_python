class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

#  Генерирует экземпляр суперкласса
def raiser0():
    X = General()
    raise X


#  Генерирует экземпляр подкласса
def raiser1():
    X = Specific1()
    raise X

#  Генерирует экземпляр другого подкласса
def raiser2():
    X = Specific2()
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    #  Соответствует суперклассу General или любому его подклассу
    except General:
        import sys
        print('caught: %s' % sys.exc_info()[0])


