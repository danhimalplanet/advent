"""Test example puzzle inputs.

run with:
pytest day16/
"""
import pytest
from aoc.day16 import Day16

test_input = """
1
2
3
"""

def test_part_1():
    assert Day16.part1_result(test_input) == 0, "failed day16 part I"

def test_part_2():
    assert Day16.part2_result(test_input) == 0, "failed day16 part II"
