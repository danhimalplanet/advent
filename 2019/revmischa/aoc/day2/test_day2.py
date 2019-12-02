"""Test example puzzle inputs.

run with:
pytest day2/
"""
import pytest
from aoc.day2 import Day2

test_input = """2,4,4,5,99,0"""

def test_part_1():
    assert Day2.part1_result(test_input) == [2,4,4,5,99,9801], "failed day2 part I"

def test_part_2():
    assert Day2.part2_result(test_input) == 0, "failed day2 part II"
