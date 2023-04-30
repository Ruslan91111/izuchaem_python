import requests


def len_joke():
    """Вернет длину строки - шутки."""
    joke = get_joke()
    # Строка кода, чтобы наглядно показать, как при тестировании переменная joke
    # будет заменена на mock. В 'main.py' будет шутка, в 'test_main.py' будет 'one'.
    print('The joke from get_joke():', joke)
    return len(joke)


def get_joke():
    """Получить шутку по API"""
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = 'no jokes'
    return joke


if __name__ == '__main__':
    print(get_joke())
    print(len_joke())
