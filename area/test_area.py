import unittest

from area import calculate_square_area


class TestSquareArea(unittest.TestCase):
    def test_area_logic(self):
        """
        Ensure that our function has the correct logic
        """
        self.assertEqual(calculate_square_area(2), 4)
        self.assertEqual(calculate_square_area(3), 9)

    def test_handle_strings(self):
        """
        Convert strings to numbers and then calculate their area
        """
        self.assertEqual(calculate_square_area("2"), 4)
        self.assertEqual(calculate_square_area("3"), 9)

    def test_handle_non_numbers(self):
        """
        Ensure that we return -1 when the input cannot be converted into a number
        """
        self.assertEqual(calculate_square_area("a"), -1)
