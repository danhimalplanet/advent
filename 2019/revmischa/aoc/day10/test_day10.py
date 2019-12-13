"""Test example puzzle inputs.

run with:
pytest day10/
"""
import pytest
from aoc.day10 import Day10

test_input = """.#..#
.....
#####
....#
...##"""

def test_part_1():
    assert Day10.part1_result(test_input) == 8, "failed day10 part I"

def test_part_2():
    assert Day10.part2_result(test_input) == 0, "failed day10 part II"
