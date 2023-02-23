import unittest

from lesson17 import my_func


class MyTestCase(unittest.TestCase):
    def test_something1(self):
        actual = my_func(1 , 7)
        self.assertEqual(actual, 8)
    def test_something2(self):
        actual = my_func(7 , 7)
        self.assertEqual(actual, 823543)
    def test_something3(self):
        actual = my_func(7 , 3)
        self.assertEqual(actual, 4)
    def test_something_fail(self):
        actual = my_func(1 , 7)
        self.assertEqual(actual, 9)

if __name__ == '__main__':
    unittest.main()
