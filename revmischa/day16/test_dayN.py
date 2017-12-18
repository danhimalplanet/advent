"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN

test_input = """s1,x3/4,pe/b"""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(DayN.part1_result(test_input, size=5), 'baedc')

    def test_part_2(self):
        self.assertEqual(DayN.part2_result(test_input, size=5, moves=2), 'ceadb')
