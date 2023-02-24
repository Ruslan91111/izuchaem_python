# Пишем свой собственный менеджер контекста.

# Необходимый минимум функциональности контекстного менеджера
# требует методов __enter__ и __exit__.


# Создаем класс контекст менеджера
class File(object):
    # При инициализации объекта принимает два аргумента.
    def __init__(self, file_name, method):
        # Переменной присваивает ссылку на открытый файл и используемый метод.
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    # Метод __exit__ принимает три аргумента.
    # Они обязательны для любого метода __exit__ класса
    # контекстного менеджера.
    def __exit__(self, type, value, traceback):
        self.file_obj.close()


# Создается экземпляр класса File, передаем два аргумента:
# 1-имя файла, 2-метод: запись. Присваиваем псевдоним в рамках менеджера
# созданному экземпляру opened_file.
with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')


#     def __exit__(self, type, value, traceback):
# При возникновении исключения, Python передает тип, значение
# и обратную трассировку исключения методу __exit__

# with File('demo.txt', 'w') as opened_file:
#     opened_file.undefined_function('Hola!')
# AttributeError: '_io.TextIOWrapper' object has no attribute 'undefined_function'



# Тип, значение и обратная трассировка ошибки передается в метод
# Обработка исключения передается методу __exit__
# Если __exit__ возвращает True, то исключение было корректно обработано.
# При возврате любого другого значения with вызывает исключение.

# Второй класс контекстного менеджера,
# На этот раз обрабатывающий исключение.
class File2(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        # Обрабатываем исключение в методе exit.
        print("Исключение было обработано")
        self.file_obj.close()
        return True


with File2('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

# Наш метод __exit__ возвращает True, таким образом with не вызывает исключение.





