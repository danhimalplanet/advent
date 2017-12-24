"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN, run_part2

test_input = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        pass
        # self.assertEqual(DayN.part1_result(test_input), 4)

    def test_part_2(self):
        ti2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""
        self.assertEqual(run_part2(ti2), 3)
