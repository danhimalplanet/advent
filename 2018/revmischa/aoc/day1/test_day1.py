"""Test example puzzle inputs.

run with:
pytest day1/
"""
import pytest
from aoc.day1 import Day1

test_input = """
1
2
3
"""

def test_part_1():
    assert Day1.part1_result(test_input) == 0, "failed day1 part I"

def test_part_2():
    assert Day1.part2_result(test_input) == 0, "failed day1 part II"
