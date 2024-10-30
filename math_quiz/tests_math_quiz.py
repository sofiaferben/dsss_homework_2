
import unittest
from math_quiz import generate_random_integer, select_random_operator, calculate_expression

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """Test if random numbers generated are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_operator(self):
        """Test if the randomly selected operator is valid."""
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random selections
            operator = select_random_operator()
            self.assertIn(operator, valid_operators)  # Ensure the operator is one of the valid ones

    def test_calculate_expression(self):
        """Test various arithmetic operations to ensure correct calculations."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 0, '*', '10 * 0', 0),  # Edge case with multiplication by zero
            (0, 5, '*', '0 * 5', 0),    # Edge case with zero multiplied
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem)  # Check if the generated problem matches the expected
            self.assertEqual(answer, expected_answer)     # Check if the calculated answer matches the expected

if __name__ == "__main__":
    unittest.main()
