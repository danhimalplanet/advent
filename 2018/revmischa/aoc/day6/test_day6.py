"""Test example puzzle inputs.

run with:
pytest day6/
"""
import pytest
from aoc.day6 import Day6

test_input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

def test_part_1():
    assert Day6.part1_result(test_input) == 17, "failed day6 part I"

def test_part_2():
    assert Day6.part2_result(test_input) == 16, "failed day6 part II"
