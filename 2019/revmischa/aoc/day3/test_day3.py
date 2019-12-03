"""Test example puzzle inputs.

run with:
pytest day3/
"""
import pytest
from aoc.day3 import Day3

# test_input = """R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83"""
test_input = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""

def test_part_1():
    assert Day3.part1_result(test_input) == 135, "failed day3 part I"

def test_part_2():
    assert Day3.part2_result(test_input) == 410, "failed day3 part II"
