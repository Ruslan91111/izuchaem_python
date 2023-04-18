class Engine:
    def __init__(self, volume):
        self.volume = volume

    def breakdown(self):
        return f"My volume - {self.volume}, but I'm broke"


class Car:
    def __init__(self, name, volume):
        self.name = name
        self.engine = Engine(volume)  # Атрибуту объекта присваиваем объект другого класса.

    def __str__(self):
        return f"I'm a {self.name}"


BMW = Car('BMW', 1500)

print(BMW.engine.breakdown())




