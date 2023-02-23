import unittest

from lesson17 import Human


class HumanTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("\tsetUp")
        self.human = Human("Andrii", 36, "male")

    def tearDown(self):
        print("\ttearDown")

    def test_something_1(self):
        print("\t\ttest_something_1")

        introduce = self.human.introduce()
        self.assertEqual(introduce, "Hi, my name is Andrii. I am 36 years old and I am male.")

    def test_something_2(self):
        print("\t\ttest_something_2")
        introduce = self.human.introduce()
        self.assertEqual(introduce, "Hi, my name is Andrii. I am 36 years old and I am male.")
