"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN

test_input = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(DayN.part1_result(test_input), 31)

    def test_part_2(self):
        self.assertEqual(DayN.part2_result(test_input), 0)
