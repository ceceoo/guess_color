import unittest
import guess
import random
real = ["red", "blue", "yellow", "green"]

class MyTestCase(unittest.TestCase):
    def test_empty(self):
        guess_num = []
        self.assertEqual(-1, guess.guess_color(real, guess_num))

    def test_inequal_length(self):
        guess_num = ["red, blue"]
        self.assertEqual(-1, guess.guess_color(real, guess_num))

    def test_success(self):
        guess_num = ["red", "blue", "yellow", "green"]
        self.assertEqual((4, 0), guess.guess_color(real, guess_num))

    def test_failure(self):
        guess_num = ["red", "pink", "yellow", "green"]
        self.assertEqual((3, 0), guess.guess_color(real, guess_num))

if __name__ == '__main__':
    unittest.main()
