class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    # Классовый метод, проверяет, что координата - то целое число.
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

    # Проверим, что координата соответствует типу int,
    # а именно: вызовем классовый метод verify_coord
    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        # Если проверку проходит, то записываем
        self._y = coord

    @property
    def z(self):
        return self._z

    # Проверим, что координата соответствует типу int,
    # а именно: вызовем классовый метод verify_coord
    @x.setter
    def z(self, coord):
        self.verify_coord(coord)
        # Если проверку проходит, то записываем
        self._z = coord

p = Point3D(1,2,3)
print(p.__dict__)