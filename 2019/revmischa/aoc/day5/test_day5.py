"""Test example puzzle inputs.

run with:
pytest day5/
"""
import pytest
from aoc.day5 import Day5

test_input = """
1
2
3
"""

def test_part_1():
    assert Day5.part1_result(test_input) == 0, "failed day5 part I"

def test_part_2():
    assert Day5.part2_result(test_input) == 0, "failed day5 part II"
