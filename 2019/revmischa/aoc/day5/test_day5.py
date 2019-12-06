"""Test example puzzle inputs.

run with:
pytest day5/
"""
import pytest
from aoc.day5 import Day5


def test_part_2():
    assert Day5.part2_result('3,9,8,9,10,9,4,9,99,-1,8', inputs=[8]) == [1]
    assert Day5.part2_result('3,9,8,9,10,9,4,9,99,-1,8', inputs=[9]) == [0]
    assert Day5.part2_result('3,9,7,9,10,9,4,9,99,-1,8', inputs=[7]) == [1]
    assert Day5.part2_result('3,9,7,9,10,9,4,9,99,-1,8', inputs=[9]) == [0]
    assert Day5.part2_result('3,3,1108,-1,8,3,4,3,99', inputs=[8]) == [1]
    assert Day5.part2_result('3,3,1108,-1,8,3,4,3,99', inputs=[7]) == [0]
    assert Day5.part2_result('3,3,1107,-1,8,3,4,3,99', inputs=[7]) == [1]
    assert Day5.part2_result('3,3,1107,-1,8,3,4,3,99', inputs=[9]) == [0]
