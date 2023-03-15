# This is a header block example for lab 03.

# You will need to supply the following information.

# Name: Tyler Baxter
# Section: 03

import unittest
from logic import *


# You can delete pass after writing your code
class TestCases(unittest.TestCase):
    def test_is_odd(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(-1))
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(-2))

    def test_in_an_interval(self):
        self.assertFalse(in_an_interval(-12))
        self.assertTrue(in_an_interval(-1))
        self.assertFalse(in_an_interval(9))
        self.assertTrue(in_an_interval(34))
        self.assertFalse(in_an_interval(52))
        self.assertTrue(in_an_interval(147))

    def test_is_divisible_in_interval(self):
        self.assertTrue(is_divisible_in_interval(100, 50))
        self.assertFalse(is_divisible_in_interval(80, 20))
        self.assertFalse(is_divisible_in_interval(85, 35))
        self.assertFalse(is_divisible_in_interval(55, 32))
        self.assertTrue(is_divisible_in_interval(110, 55))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
