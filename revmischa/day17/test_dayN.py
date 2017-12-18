"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(DayN(3, 2017).run_part1(), 638)

    def test_part_2(self):
        self.assertEqual(DayN(3, 2017).run_part2(), 0)
