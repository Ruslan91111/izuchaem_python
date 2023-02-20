class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Имя {self.name}\tВозраст: {self.age}")


tom = Person("Tom")
tom.name = "Spiderman"
tom.age = -29
tom.display_info()


#
class Person2:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    def set_age(self, age):
        if 1 < age < 100:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


tom2 = Person2("Tom2")
tom2.display_info()
tom2.set_age(-222)
tom2.set_age(25)
tom2.display_info()


# Для создания приватного атрибута в начале его наименования
# ставится двойной прочерк: self.__name.
# К такому атрибуту мы сможем обратиться только из того же класса.
# Но не сможем обратиться вне этого класса. Например, присвоение
# значения этому атрибуту ничего не даст:


# Аннотация свойств
# Для создания свойства-геттера над свойством ставится аннотация @property.
# Для создания свойства-сеттера над свойством устанавливается
# аннотация имя_свойства_геттера.setter.

class Person3:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    # Также можно добавить любой функционал
    # def age(self, age):
    #     new_age = age + 300
    #     self.__age = new_age




    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


p = Person3('alex')
p.age = 22
p.display_info()
