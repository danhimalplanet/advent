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
        self.assertEqual(DayN.part1_result('ne,ne,ne'), 3)
        self.assertEqual(DayN.part1_result('ne,ne,sw,sw'), 0)
        self.assertEqual(DayN.part1_result('ne,ne,s,s'), 2)
        self.assertEqual(DayN.part1_result('se,sw,se,sw,sw'), 3)

    def test_part_2(self):
        self.assertEqual(DayN.part2_result(test_input), 0)
