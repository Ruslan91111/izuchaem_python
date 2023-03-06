import asyncio


# Функция, имитирующая асинхронное соединения с некой периферией
async def get_conn(host, port):
    # Содержит класс
    class Conn:
        # Имитируем отправку данных
        async def put_data(self):
            print('Отправка данных...')
            # Ожидание.
            await asyncio.sleep(2)
            # Отправлены.
            print('Данные отправлены.')

        async def get_data(self):
            # Имитируем получение данных
            print('Получение данных...')
            # Ожидание.
            await asyncio.sleep(2)
            # Получены.
            print('Данные получены.')

        async def close(self):
            # Имитируем закрытие соединения
            print('Завершение соединения...')
            # Ожидание
            await asyncio.sleep(2)
            # Завершено
            print('Соединение завершено.')

    print('Устанавливаем соединение...')
    await asyncio.sleep(2)
    print('Соединение установлено.')
    return Conn()


class Connection:
    # Этот конструктор будет выполнен в заголовке with при создании экземпляра.
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # этот метод будет неявно выполнен при входе в with
    async def __aenter__(self):
        # Присваиваем ссылку на функцию вне класса,
        # передаем аргументы host и post.
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    # этот метод будет неявно выполнен при выходе из with
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # метод закрытие
        await self.conn.close()


# Главная вызывающая функция.
async def main():
    # Запускаем контекст менеджер, создаем экземпляр класса, передаем 2 аргумента,
    # для проброса в функцию get_conn.
    async with Connection('localhost', 9001) as conn:
        # Создаем задачу(имитируем отправку данных).
        send_task = asyncio.create_task(conn.put_data())
        # Создаем задачу(имитируем получение данных).
        receive_task = asyncio.create_task(conn.get_data())

        # Операции отправки и получения данных выполняем конкурентно.
        # Создаем для каждой задачи точку переключения.
        await send_task
        await receive_task


# Запускаем главную функцию.
asyncio.run(main())       





