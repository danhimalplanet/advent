import unittest
from dayN import Memory


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        t = Memory.new_from_puzzle_input("0 2 7 0")
        self.assertEqual(t.run_part1(), 5)

    def test_part_2(self):
        t = Memory.new_from_puzzle_input("0 2 7 0")
        self.assertEqual(t.run_part2(), 4)
