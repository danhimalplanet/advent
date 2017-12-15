"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN

test_input = """0: 3
1: 2
4: 4
6: 4"""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(DayN.part1_result(test_input), 24)

    def test_part_2(self):
        self.assertEqual(DayN.part2_result(test_input), 10)
