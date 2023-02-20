import unittest
from izuchaem_python.random_code.descriptors import Car2

class TestCat(unittest.TestCase):
    def test_init(self):
        bmw = Car2("BMW", "X7", 45)
        expected = {'make': 'BMW', 'model': 'X7'}
        self.assertEqual(expected, bmw.__dict__)





