class Spam:
    def doit(self, message):
        print(message)

obj = Spam()
obj.doit('Hello World')

obj =  Spam()
х = obj.doit         #Объект  связанного метода: экземпляр + функция
х('hello world')          #Тот же  эффект,  что  и objectl.doit

obj = Spam()
t = Spam.doit                # Объект несвязанного метода (функция в Python З.Х: см. далее)
t(obj, 'howdy')          # Передача экземпляра (если метод его ожидает в Python З.Х)


class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        х = self.m1    # Еще один объект связанного метода
        х(42)          # Выглядит подобно простой функции

Eggs().m2()            # Выводит 42

