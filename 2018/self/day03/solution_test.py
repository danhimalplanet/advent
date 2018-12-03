#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from solution import part1, part2


class TestPart1(unittest.TestCase):
    def setUp(self):
        self.input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        self.output = 4

    def test_it(self):
        overlap, fabric = part1(self.input)
        self.assertEqual(overlap, self.output)


class TestPart2(unittest.TestCase):
    def setUp(self):
        self.input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        self.output = "#3"

    def test_it(self):
        overlap, fabric = part1(self.input)
        self.assertEqual(part2(self.input, fabric), self.output)



if __name__ == '__main__':
    unittest.main()

# eof
