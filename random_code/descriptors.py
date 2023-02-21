# Класс без дескриптора.
# В __init__ мы задаем проверки для поля, но из-за этого некрасиво(раздуто).
# Также эти проверки не будут работать для присваивания значения атрибуту.
class Car:
    def __init__(self, make, model, fuel_cap):
        self.make = make
        self.model = model
        self.fuel_cap = fuel_cap
        # Проверка, что название производителя состоит из букв
        if isinstance(self.make, str):
            print(self.make)
        else:
            raise ValueError("Make of the car can never be an integer")

        # Проверка, что бензиновый бак положительное число.
        if self.fuel_cap < 0:
            raise ValueError("Fuel capacity can never be less than zero")

    def __str__(self):
        return "{0} model {1} with a fuel capacity of " \
               "{2}ltr.".format(self.make, self.model, self.fuel_cap)


car1 = Car("BMW", "X7", 40)
print(car1)


# Но все это работает(проверки поля на валидность данных)
# только при инициализации экземпляра.
# Вот для чего и нужны дескрипторы.


# Класс дескриптор для поля fuel_cap
class Descriptor:
    def __init__(self):
        self.__fuel_cap = 0

    def __get__(self, instance, owner):
        return self.__fuel_cap

    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("Fuel capacity can only be an integer")

        if value < 0:
            raise ValueError("Fuel capacity can never be less than zero")

        self.__fuel_cap = value

    def __delete__(self, instance):
        del self.__fuel_cap


class Car2:
    # Ссылка полю на класс - дескриптор
    fuel_cap = Descriptor()

    def __init__(self, make, model, fuel_cap):
        self.make = make
        self.model = model
        self.fuel_cap = fuel_cap

    def __str__(self):
        return "{0} model {1} with a fuel capacity of " \
               "{2}ltr.".format(self.make, self.model, self.fuel_cap)


car2 = Car2("BMW", "X7", 45)
print(car2)
print(car2.__dict__)
print(car2.fuel_cap)







