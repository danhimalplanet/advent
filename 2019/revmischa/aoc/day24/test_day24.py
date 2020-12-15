"""Test example puzzle inputs.

run with:
pytest day24/
"""
import pytest
from aoc.day24 import Day24

test_input = """....#
#..#.
#..##
..#..
#...."""

def test_part_1():
    assert Day24.part1_result(test_input) == 2129920, "failed day24 part I"

def test_part_2():
    assert Day24.part2_result(test_input) == 99, "failed day24 part II"
