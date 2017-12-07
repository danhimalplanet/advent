"""Test example puzzle inputs.

run with:
pytest dayX/
"""

import unittest
from .dayN import DayN

test_input = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""


class DayNTestCase(unittest.TestCase):
    def test_part_1(self):
        t = DayN.new_from_puzzle_input(test_input)
        self.assertEqual(t.run_part1().name, 'tknk')

    def test_part_2_root_weight(self):
        t = DayN.new_from_puzzle_input(test_input)
        root = t.gen_graph()
        ugml = root.child_nodes[2]
        padx = root.child_nodes[1]
        fwft = root.child_nodes[0]
        self.assertEqual(ugml.weight_with_children(), 251)
        self.assertEqual(padx.weight_with_children(), 243)
        self.assertEqual(fwft.weight_with_children(), 243)

    def test_part_2(self):
        t = DayN.new_from_puzzle_input(test_input)
        root = t.gen_graph()
        unbalanced = root.find_unbalanced()

        self.assertEqual(unbalanced, 60)
