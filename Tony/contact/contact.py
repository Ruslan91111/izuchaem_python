"""
Класс Contact содержит контактную информацию
Расписывается инициализатор, геттеры и сеттеры, а также __str__
"""

class Contact:
    # инициализирует атрибуты
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # устанавливают атрибуты
    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def  set_email(self, email):
        self.__email = email

    # возвращают атрибуты
    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    # метод __str__ возвраащает состояние объекта
    # в виде строкового значения
    def __str__(self):
        return f'Имя: {self.__name}\n' + \
            f'Телефон: {self.__phone}\n' + \
            f'Электронная почта: {self.__email}\n'




