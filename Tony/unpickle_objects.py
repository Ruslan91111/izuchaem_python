""" Распаковать данные из файла посредством pickle.load()"""
import pickle


def main():
    end_of_file = False
    input_file = open('info.dat', 'rb')

    while not end_of_file:
        try:
            person = pickle.load(input_file)
            display_data(person)

        except EOFError:
            end_of_file = True

    input_file.close()


def display_data(person):
    print('name - ', person['name'])
    print('age - ', person['age'])
    print('weight - ', person['weight'])
    print()


if __name__ == '__main__':
    main()


