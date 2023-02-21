# Первый класс без использования дескрипторов.
# Для каждого атрибута определены сеттер и геттер.
class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    # Классовый метод, проверяет, что координата - это целое число.
    @classmethod
    def verify_coord(cls, coord):
        if not isinstance(coord, int):
            raise TypeError("Coord must be a integer")

    # Геттер
    @property
    def x(self):
        return self._x

    # Проверим, что координата соответствует типу int,
    # а именно: вызовем классовый метод verify_coord
    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        # Если проверку проходит, то записываем
        self._x = coord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        # Если проверку проходит, то записываем
        self._y = coord

    @property
    def z(self):
        return self._z

    @x.setter
    def z(self, coord):
        self.verify_coord(coord)
        # Если проверку проходит, то записываем
        self._z = coord


p = Point3D(1, 2, 3)
print(p.__dict__)


# Создаем дескриптор - класс со связанным поведением (binding behavior)
class Integer:
    # owner - ссылка на класс внутри которого используется дескриптор
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        instance.__dict__[self.name] = value
# owner - принимает ссылку на класс, внутри которого используется дескриптор.


class Point3D2:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Классовый метод, проверяет, что координата - это целое число.
    @classmethod
    def verify_coord(cls, coord):
        if not isinstance(coord, int):
            raise TypeError("Coord must be an integer")


p = Point3D2(1, 2, 3)
print(p.__dict__)



