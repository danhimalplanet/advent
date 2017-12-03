import unittest
from day3 import Board


class Day3TestCase(unittest.TestCase):
    def test_distances(self):
        """
        Data from square 1 is carried 0 steps, since it's at the access port.
        Data from square 12 is carried 3 steps, such as: down, left, left.
        Data from square 23 is carried only 2 steps: up twice.
        Data from square 1024 must be carried 31 steps.
        """
        self.assertEqual(Board(starting_loc=1).distance(), 0)
        self.assertEqual(Board(starting_loc=12).distance(), 3)
        self.assertEqual(Board(starting_loc=23).distance(), 2)
        self.assertEqual(Board(starting_loc=1024).distance(), 31)

    def test_distances_sum(self):
        """
        Square 1 starts with the value 1.
        Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
        Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
        Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
        Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
        """
        self.assertEqual(Board(starting_loc=1, use_sum=True).loc_coords(), 1)
        self.assertEqual(Board(starting_loc=2, use_sum=True).loc_coords(), 1)
        self.assertEqual(Board(starting_loc=3, use_sum=True).loc_coords(), 2)
        self.assertEqual(Board(starting_loc=4, use_sum=True).loc_coords(), 4)
        self.assertEqual(Board(starting_loc=5, use_sum=True).loc_coords(), 5)
