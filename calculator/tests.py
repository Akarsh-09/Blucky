# calculator/tests.py

import unittest
import math
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calculator.evaluate("10 / 2")
        self.assertEqual(result, 5)

    def test_power(self):
        result = self.calculator.evaluate("3 ^ 5")
        # 3^5 = 243
        self.assertEqual(result, 243)

    def test_power_with_zero(self):
        result = self.calculator.evaluate("10 ^ 0")
        self.assertEqual(result, 1)

    def test_power_with_one(self):
        result = self.calculator.evaluate("10 ^ 1")
        self.assertEqual(result, 10)

    def test_nested_expression(self):
        result = self.calculator.evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self):
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    def test_expression_with_power(self):
        result = self.calculator.evaluate("3 ^ 2 + 2")
        # Power has higher precedence than +
        # So it should be (3^2) + 2 = 9 + 2 = 11
        self.assertEqual(result, 11)

    def test_empty_expression(self):
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")

    # --- New Tests ---

    def test_floats(self):
        result = self.calculator.evaluate("2.5 + 3.5")
        self.assertEqual(result, 6.0)
        result = self.calculator.evaluate("10.5 / 2")
        self.assertEqual(result, 5.25)

    def test_parentheses(self):
        # Test simple parentheses
        result = self.calculator.evaluate("(3 + 5) * 2")
        self.assertEqual(result, 16)
        # Test nested parentheses
        result = self.calculator.evaluate("2 * (3 + (4 / 2))")
        self.assertEqual(result, 10)

    def test_mismatched_parentheses_open(self):
        with self.assertRaisesRegex(ValueError, "mismatched parentheses"):
            self.calculator.evaluate("(3 + 5")

    def test_mismatched_parentheses_close(self):
        with self.assertRaisesRegex(ValueError, "mismatched parentheses"):
            self.calculator.evaluate("3 + 5)")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.evaluate("10 / 0")

    def test_unary_sqrt(self):
        result = self.calculator.evaluate("sqrt 16")
        self.assertEqual(result, 4.0)
        result = self.calculator.evaluate("sqrt 2")
        self.assertAlmostEqual(result, 1.41421356, places=7)

    def test_unary_log(self):
        result = self.calculator.evaluate("log 100")
        self.assertEqual(result, 2.0)

    def test_unary_ln(self):
        result = self.calculator.evaluate("ln 2.718281828459")
        self.assertAlmostEqual(result, 1.0, places=7)

    def test_unary_sin(self):
        # sin(90) = 1
        result = self.calculator.evaluate("sin 90")
        self.assertAlmostEqual(result, 1.0, places=7)

    def test_unary_cos(self):
        # cos(0) = 1
        result = self.calculator.evaluate("cos 0")
        self.assertAlmostEqual(result, 1.0, places=7)

    def test_unary_tan(self):
        # tan(45) = 1
        result = self.calculator.evaluate("tan 45")
        self.assertAlmostEqual(result, 1.0, places=7)

    def test_unary_precedence(self):
        # sqrt 16 + 2 should be 4 + 2 = 6
        result = self.calculator.evaluate("sqrt 16 + 2")
        self.assertEqual(result, 6.0)
        # 2 * sqrt 16 should be 2 * 4 = 8
        result = self.calculator.evaluate("2 * sqrt 16")
        self.assertEqual(result, 8.0)

    def test_unary_not_enough_operands(self):
        with self.assertRaisesRegex(ValueError, "not enough operands for unary operator"):
            self.calculator.evaluate("sqrt")

    def test_invalid_expression_structure(self):
        # Multiple operators in a row (not supported by this implementation, should raise ValueError)
        with self.assertRaises(ValueError):
            self.calculator.evaluate("3 ++ 5")
        # Expression ending with operator
        with self.assertRaises(ValueError):
            self.calculator.evaluate("3 +")

    def test_invalid_token(self):
        with self.assertRaisesRegex(ValueError, "invalid token"):
            self.calculator.evaluate("3 + abc")

    def test_math_errors(self):
        # sqrt of negative number
        with self.assertRaises(ValueError):
            self.calculator.evaluate("sqrt -1")
        # log of negative number
        with self.assertRaises(ValueError):
            self.calculator.evaluate("log -1")


if __name__ == "__main__":
    unittest.main()
