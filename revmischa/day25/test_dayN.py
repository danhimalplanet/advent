"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN

test_input = """In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A."""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(DayN.part1_result(test_input, rounds=6), 3)

    def test_part_2(self):
        self.assertEqual(DayN.part2_result(test_input, rounds=0), 0)
