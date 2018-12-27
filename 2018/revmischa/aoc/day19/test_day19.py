"""Test example puzzle inputs.

run with:
pytest day19/
"""
import pytest
from aoc.day19 import Day19

test_input = """
1
2
3
"""

def test_part_1():
    assert Day19.part1_result(test_input) == 0, "failed day19 part I"

def test_part_2():
    assert Day19.part2_result(test_input) == 0, "failed day19 part II"
