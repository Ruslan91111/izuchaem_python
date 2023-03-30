"""Пользователь вводит три буквы, программа находит количество вхождений
указанной последовательности из трех букв в текстовом файле"""


def main():
    print('Последовательно введите три буквы, которые нужно найти')
    letter1 = input('Введите первую букву - ')
    letter2 = input('Введите вторую букву - ')
    letter3 = input('Ввдите третью букву - ')
    count = 0
    with open('test.txt', 'r') as file:
        text = file.read()
        for i in range(1, len(text)):
            if text[i] == letter1 and text[i+1] == letter2 and text[i+2] == letter3:
                count += 1

    print(f'сочетание букв "{letter1}{letter2}{letter3}" в файле "test.txt" встречается {count}')


if __name__ == '__main__':
    main()





