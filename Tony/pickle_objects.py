""" Ввести данные и упаковать их в файл посредством pickle"""
import pickle


def main():
    again = 'д'
    output_file = open('info.dat', 'wb')

    while again.lower() == 'д':
        save_data(output_file)

        again = input('Желаете ввести еще данные ? (д/н): ')

    output_file.close()


def save_data(file):
    person = {}
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = int(input('Weight: '))

    pickle.dump(person, file)


if __name__ == '__main__':
    main()


