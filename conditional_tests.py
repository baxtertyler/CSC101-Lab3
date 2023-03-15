# This is a header block example for lab 03.

# You will need to supply the following information.

# Name: Tyler Baxter
# Section: 03

import unittest
from conditional import *


# You can delete pass after writing your code
class TestCases(unittest.TestCase):
    def test_min_of_2(self):
        self.assertEqual(min_of_2(1, 2), 1)
        self.assertEqual(min_of_2(-5, 10), -5)
        self.assertEqual(min_of_2(-10, -5), -10)

    def test_min_of_3(self):
        self.assertEqual(min_of_3(1, 2, 3), 1)
        self.assertEqual(min_of_3(-5, 0, 5), -5)
        self.assertEqual(min_of_3(-15, -10, -5), -15)

    def test_rental_late_fee(self):
        self.assertEqual(rental_late_fee(2), 0)
        self.assertEqual(rental_late_fee(5), 10)
        self.assertEqual(rental_late_fee(12), 15)
        self.assertEqual(rental_late_fee(22), 30)
        self.assertEqual(rental_late_fee(23), 100)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
