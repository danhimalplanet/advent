"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN

test_input = """
1
2
3
"""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        t = DayN.new_from_puzzle_input(test_input)
        self.assertEqual(t.run_part1(), 0)

    def test_part_2(self):
        t = DayN.new_from_puzzle_input(test_input)
        self.assertEqual(t.run_part2(), 0)
