"""Test example puzzle inputs.

run with:
pytest day2/
"""
import pytest
from aoc.day2 import Day2

test_input = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
"""

def test_part_1():
    assert Day2.part1_result(test_input) == 12, "failed day2 part I"

def test_part_2():
    d2 = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
"""
    assert Day2.part2_result(d2) == 'fgij', "failed day2 part II"
