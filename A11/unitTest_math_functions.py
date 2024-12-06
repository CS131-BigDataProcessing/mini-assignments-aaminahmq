
import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):

    #power function testd
    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)

    # divide function tests
    def test_divide_positive(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(6, 0)

    def test_divide_negative(self):
        self.assertEqual(divide(-6, 3), -2)

if __name__ == "__main__":
    unittest.main()

