# Приложение, которое узнает погоду в разных городах при помощи
# библиотеки aiohttp и API-сервиса openweathermap.org.

# Используем два вложенных менеджера контекста:
# для сессии и для функции get. Так требует документация aiohttp.

import time
import asyncio
from aiohttp import ClientSession


# Асинхронная функция
async def get_weather(city):
    # Асинхронный менеджер контекста.
    async with ClientSession() as session:
        # Открываем ClientSession как session.
        # url, по которому будем обращаться.
        url = f'http://api.openweathermap.org/data/2.5/weather'
        # Ключик к API.
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        # Еще один асинхронный менеджер контекста.
        async with session.get(url=url, params=params) as response:
            # Сохраняем Json из ответа.
            weather_json = await response.json()
            # Выводим полученную JSON информацию.
            # print(weather_json)
            print(f'{city}: {weather_json["weather"][0]["main"]}')


# Главная асинхронная функция.
async def main(cities_):
    tasks = []

    # Перебираем список городов.
    for city in cities_:
        # Наполняем список задачами из функции get_weather для соответствующего
        # города, передаваемого в ключик к API.
        tasks.append(asyncio.create_task(get_weather(city)))

    # Запускаем асинхронные задачи в цикле for.
    for task in tasks:
        await task

cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


print(time.strftime('%X'))
# Запускаем
asyncio.run(main(cities))

print(time.strftime('%X'))
# Время выполнения секунда.


