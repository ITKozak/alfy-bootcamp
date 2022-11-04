#! /usr/bin/python

# Import module for unit testing
import unittest

# Trying to import expressions module from working dirrectory.
# If there aren't any - prints error and switch run_tests flag.
try:
    from expressions import *
    run_tests = True
except ImportError as e:
    print(f"ERROR - {e}\nCheck if your expressions.py file correctly named or exist in this folder and try again.")
    run_tests = False


# Declaration of test class and corresponding methods.
class Tests(unittest.TestCase):
    def test_calc_math_expr(self):
        self.assertEqual(calc_math_expression_from_str("10 : 2"), 5.0)
        self.assertEqual(calc_math_expression_from_str("10 : -2"), -5.0)
        self.assertEqual(calc_math_expression_from_str("-10 : -2"), 5.0)
        self.assertEqual(calc_math_expression_from_str("-10 : 2"), -5.0)
        self.assertEqual(calc_math_expression_from_str("10 + 2"), 12.0)
        self.assertEqual(calc_math_expression_from_str("100 - 39.3"), 60.7)
        self.assertEqual(calc_math_expression_from_str("5 : 2"), 2.5)
        self.assertIsNone(calc_math_expression_from_str("5 : 0"), None)
        self.assertIsNone(calc_math_expression_from_str("10 333 2"), None)
        self.assertIsNone(calc_math_expression_from_str("10 ^ 2"), None)

    def test_larg_small(self):
        self.assertEqual(find_largest_and_smallest_numbers(5, 1, 10), (10, 1))
        self.assertEqual(find_largest_and_smallest_numbers(2.5, 2.5, 7), (7, 2.5))
        self.assertEqual(find_largest_and_smallest_numbers(7, 2.5, 2.5), (7, 2.5))
        self.assertEqual(find_largest_and_smallest_numbers(-5, -5, -5), (-5, -5))
        self.assertEqual(find_largest_and_smallest_numbers(10, -1, 10), (10, -1))
        self.assertEqual(find_largest_and_smallest_numbers(-2, 5, -2), (5, -2))
        self.assertEqual(find_largest_and_smallest_numbers(3, 20, -2), (20, -2))
        self.assertEqual(find_largest_and_smallest_numbers(7, 10, 0), (10, 0))
        self.assertEqual(find_largest_and_smallest_numbers(10, 7, 0), (10, 0))
        self.assertEqual(find_largest_and_smallest_numbers(0, 10.01, 10), (10.01, 0))

    def test_quadratic(self):
        self.assertEqual(quadratic_equation_solver(1, 1.5, -1), (0.5, -2))
        self.assertEqual(quadratic_equation_solver(1, -8, 16), (4, None))
        self.assertEqual(quadratic_equation_solver(1, -2, 34.5), (None, None))
        self.assertEqual(quadratic_equation_solver(4, -12, 9), (3/2, None))

    def test_temp(self):
        self.assertTrue(temp_checker(26, 38, 90, 20))
        self.assertFalse(temp_checker(10, 10, 10, 10))
        self.assertTrue(temp_checker(10, 11, 10, 11))
        self.assertTrue(temp_checker(-1, -9, 0, 1))
        self.assertTrue(temp_checker(0, 90, 0, 1))

# Main body.
# If expressions.py have had some errors importing - skip tests.
if __name__ == "__main__":
    if run_tests:
        unittest.main()