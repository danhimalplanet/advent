"""Test example puzzle inputs.

run with:
pytest day8/
"""
import pytest
from aoc.day8 import Day8

test_input = "123456789012"


def test_part_1():
    assert Day8.part1_result(test_input, w=2, h=3) == 1, "failed day8 part I"


def test_part_2():
    assert Day8.part2_result('0222112222120000', w=2, h=2) == [['0','1'], ['1','0']], "failed day8 part II"
