#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from solution import part1, part2


class TestPart1(unittest.TestCase):
    def setUp(self):
        self.cases = [{"in": [1, -2, 3, 1], "out": 3},
                      {"in": [1, 1, 1], "out": 3},
                      {"in": [1, 1, -2], "out": 0},
                      {"in": [-1, -2, -3], "out": -6}]

    def test_it(self):
        for case in self.cases:
            self.assertEqual(part1(case["in"]), case["out"])


class TestPart2(unittest.TestCase):
    def setUp(self):
        self.cases = [{"in": [1, -2, 3, 1], "out": 2},
                      {"in": [1, -1], "out": 0},
                      {"in": [3, 3, 4 ,-2, -4], "out": 10},
                      {"in": [-6, 3, 8, 5, -6], "out": 5},
                      {"in": [7, 7, -2, -7, -4], "out": 14}]

    def test_it(self):
        for case in self.cases:
            self.assertEqual(part2(case["in"]), case["out"])



if __name__ == '__main__':
    unittest.main()

# eof
