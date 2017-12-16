"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(DayN(65, 8921).run_part1(), 588)

    def test_part_2(self):
        pass
        # self.assertEqual(DayN(65, 8921).run_part1(), 588)
