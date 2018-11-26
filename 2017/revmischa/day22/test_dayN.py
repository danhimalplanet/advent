"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN

test_input = """..#
#..
..."""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(DayN.part1_result(test_input, rounds=10000, debug=False), 5587)

    def test_part_2(self):
        self.assertEqual(DayN.part2_result(test_input, rounds=100, debug=False), 26)
        self.assertEqual(DayN.part2_result(test_input, rounds=10000000, debug=False), 2511944)
