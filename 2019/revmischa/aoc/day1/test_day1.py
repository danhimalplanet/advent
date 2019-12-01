"""Test example puzzle inputs.

run with:
pytest day1/
"""
import pytest
from aoc.day1 import Day1

test_input = """
12
14
1969
100756
"""


def test_part_1():
    assert Day1.part1_result(test_input) == 2 + 2 + 654 + 33583, "failed day1 part I"


def test_part_2():
    tot = 2 + 2 + 966 + 50346
    assert Day1.part2_result(test_input) == tot, "failed day1 part II"
