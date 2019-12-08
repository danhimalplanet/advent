"""Test example puzzle inputs.

run with:
pytest day6/
"""
import pytest
from aoc.day6 import Day6

test_input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""


def test_part_1():
    # assert Day6.part1_result(test_input) == 42, "failed day6 part I"
    pass

def test_part_2():
    ti2 = test_input + "\nK)YOU\nI)SAN"
    assert Day6.part2_result(ti2) == 4, "failed day6 part II"
