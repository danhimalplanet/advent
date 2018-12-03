"""Test example puzzle inputs.

run with:
pytest day3/
"""
import pytest
from aoc.day3 import Day3

test_input = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""

def test_part_1():
    assert Day3.part1_result(test_input) == 4, "failed day3 part I"

def test_part_2():
    assert Day3.part2_result(test_input) == 0, "failed day3 part II"
