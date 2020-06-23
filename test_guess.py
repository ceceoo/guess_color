import unittest
import guess
import random
real_set = ["red", "blue", "yellow", "green", "pink", "white"]
real = random.sample(real_set, 4)

class MyTestCase(unittest.TestCase):
    def test_empty(self):
        guess_num = []
        self.assertEqual(-1, guess.guess_color(real, guess_num))


if __name__ == '__main__':
    unittest.main()
