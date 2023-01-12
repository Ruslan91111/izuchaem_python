import contact
import pickle

# Глобальные переменные для пунктов меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Глобальная константа для имени файла
FILENAME = 'contacts.dat'

def main():
    # Загрузить существующий словарь контактов
    mycontacts = load_contacts()

    # инициализировать переменную для выбора пользователя
    choice = 0

    while choice != QUIT:
        # получить выбранный пользователем пункт меню
        choice = get_menu_choice()

        # Обработать выбранный вариант действий
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    # сохранить словарь mycontacts в файле
    save_contacts(mycontacts)


def load_contacts():
    try:
        # открыть файл contacts.dat.
        input_file = open(FILENAME, 'rb')

        # расконсервировать словарь
        contact_dct = pickle.load(input_file)

        # закрыть файл
        input_file.close()
    except IOError:
        # не получилось открыть файл, создать пустой файл
        contact_dct = {}

    return contact_dct


# выводит меню и получает проверенный на допустимость выбранный пользователем пункт.
def get_menu_choice():
    print()
    print('Меню')
    print('-------------------------------------')
    print('1. Найти контактное лицо')
    print('2. Добавить новое контактное лицо')
    print('3. Изменить существующее контактное лицо')
    print('4. Удалить контактное лицо')
    print('5. Выйти из программы')
    print()

    # выбранный пользователем пункт
    choice = int(input('Введите выбранный пункт: '))

    # проверить выбранный пункт на допустимость
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))

    # Вернуть выбранный пользователем пункт
    return choice


#  функция отыскивает элемент в заданном словаре
def look_up(mycontacts):
    # Получить искомое имя
    name = input('Введите имя: ')
    # Отыскать его в словаре
    print(mycontacts.get(name, 'Это имя не найдено.'))


# добавляет новую запись в указанный словарь
def add(mycontacts):
    # Получить контактную информацию
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input('Электронный адрес: ')

    # Создать именованную запись с объектом Contact
    entry = contact.Contact(name, phone, email)

    # Если имя не существует в словаре, то добавить его в качестве ключа со связанным с ним
    # значением в виде объекта

    if name not in mycontacts:
        mycontacts[name] = entry
        print('Запись добавлена.')
    else:
        print('Это имя уже существует.')


# изменяет текущую запись в словаре
def change(mycontacts):
    # Получить искомое имя
    name = input('Введите имя: ')

    if name in mycontacts:
        # Получить новый телефонный номер и остальные атрибуты
        phone = input('Введите новый телефонный номер: ')

        phone = input('Введите новый электронный адрес: ')

        entry = contact.Contact(name, phone, email)


        # обновить запись
        mycontacts[name] = entry
        print('Информация обновлена.')
    else:
        print('Это имя не найдено. ')


# удаляет запись
def delete(mycontacts):
    name = input('Введите имя: ')

    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена.')
    else:
        print('Это имя не найдено.')


# функция консервирует указанный объект и сохраняет его в файле контактов
def save_contacts(mycontacts):
    # открыть файл для записи
    output_file = open('FILENAME', 'wb')

    # законсервировать словарь и сохранить его в
    pickle.dump(mycontacts, output_file)

    output_file.close()

if __name__ =='__main__':
    main()


