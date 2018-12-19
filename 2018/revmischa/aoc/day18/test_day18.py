"""Test example puzzle inputs.

run with:
pytest day18/
"""
import pytest
from aoc.day18 import Day18

test_input = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""

def test_part_1():
    assert Day18.part1_result(test_input) == 1147, "failed day18 part I"

def test_part_2():
    assert Day18.part2_result(test_input) == 0, "failed day18 part II"
