from izuchaem_python.random_code.simple_hash import hash1, hash2
import unittest


class TestHash(unittest.TestCase):
    def test_hash(self):
        work_of_hash = hash1('cat', 11)
        expected = 4
        self.assertEqual(expected, work_of_hash)

    def test_hash2(self):
        work_of_hash = hash2('cat', 11)
        expected = 3
        self.assertEqual(expected, work_of_hash)

if __name__ == '__main__':
    unittest.main()







