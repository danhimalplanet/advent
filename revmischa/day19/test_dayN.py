"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN

test_input = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(DayN.part1_result(test_input), 'ABCDEF')

    def test_part_2(self):
        self.assertEqual(DayN.part2_result(test_input), 0)
