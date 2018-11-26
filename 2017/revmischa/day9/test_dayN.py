"""Test example puzzle inputs.

run with:
pytest dayX/
"""
import unittest
from .dayN import DayN


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(DayN.part1_result('{}'), 1)
        self.assertEqual(DayN.part1_result('{{{}}}'), 6)
        self.assertEqual(DayN.part1_result('{{},{}}'), 5)
        self.assertEqual(DayN.part1_result('{{{},{},{{}}}}'), 16)
        self.assertEqual(DayN.part1_result('{<a>,<a>,<a>,<a>}'), 1)
        self.assertEqual(DayN.part1_result('{{<a>},{<a>},{<a>},{<a>}}'), 9)
        self.assertEqual(DayN.part1_result('{{<!>},{<!>},{<!>},{<a>}}'), 3)
        self.assertEqual(DayN.part1_result('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
        self.assertEqual(DayN.part1_result('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
        self.assertEqual(DayN.part1_result('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)

    def test_part_2(self):
        self.assertEqual(DayN.part2_result('<>'), 0)
        self.assertEqual(DayN.part2_result('<random characters>'), 17)
        self.assertEqual(DayN.part2_result('<<<<>'), 3)
        self.assertEqual(DayN.part2_result('<{!>}>'), 2)
        self.assertEqual(DayN.part2_result('<!!>'), 0)
        self.assertEqual(DayN.part2_result('<!!!>>'), 0)
        self.assertEqual(DayN.part2_result('<{o"i!a,<{i<a>'), 10)
