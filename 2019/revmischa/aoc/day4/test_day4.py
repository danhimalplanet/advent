"""Test example puzzle inputs.

run with:
pytest day4/
"""
import pytest
from aoc.day4 import Day4

test_input = """
1
2
3
"""

def test_part_1():
    assert Day4.part1_result(test_input) == 0, "failed day4 part I"

def test_part_2():
    assert Day4.part2_result(test_input) == 0, "failed day4 part II"
