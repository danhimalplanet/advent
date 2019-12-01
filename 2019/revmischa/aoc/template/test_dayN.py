"""Test example puzzle inputs.

run with:
pytest dayN/
"""
import pytest
from aoc.dayN import DayN

test_input = """
1
2
3
"""

def test_part_1():
    assert DayN.part1_result(test_input) == 0, "failed dayN part I"

def test_part_2():
    assert DayN.part2_result(test_input) == 0, "failed dayN part II"
