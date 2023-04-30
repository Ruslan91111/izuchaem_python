import unittest
from unittest.mock import patch, MagicMock

from main import len_joke, get_joke


class TestJoke(unittest.TestCase):
    # Для проверки работы функции 'len_joke' пропатчим функцию 'get_joke' - зададим ей определенное поведение
    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(), 3)

    # Для проверки работы функции 'get_joke' пропатчим 'requests' - зададим определенное поведение.
    @patch('main.requests')
    def test_get_joke(self, mock_requests):
        # Создаем mock и задаем ему определенное поведение.
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'nice day'}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'nice day')

    #  Проверка на неполучение шутки.
    @patch('main.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)
        mock_response.json.return_value = {'value': 'nice day'}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'no jokes')



if __name__ == '__main__':
    unittest.main()