"""Test example puzzle inputs.

run with:
pytest day9/
"""
import pytest
from aoc.day9 import Day9

def test_part_1():
    assert Day9.part1_result('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99') == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    assert len(str(Day9.part1_result('1102,34915192,34915192,7,4,7,99,0')[0])) == 16
    assert Day9.part1_result('104,1125899906842624,99')[0] == 1125899906842624

def test_part_2():
    pass
    # assert Day9.part2_result(test_input) == 0, "failed day9 part II"
