"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN

test_input = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        t = DayN.new_from_puzzle_input(test_input)
        self.assertEqual(t.run_part1(), 1)

    def test_part_2(self):
        t = DayN.new_from_puzzle_input(test_input)
        self.assertEqual(t.run_part2(), 10)
