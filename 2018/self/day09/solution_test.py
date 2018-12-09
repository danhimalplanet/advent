#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from solution import play


class TestPlay(unittest.TestCase):
    def setUp(self):
        self.cases = [{"in": [9, 25], "out": 32},
                      {"in": [10, 1618], "out": 8317},
                      {"in": [13, 7999], "out": 146373},
                      {"in": [17, 1104], "out": 2764},
                      {"in": [21, 6111], "out": 54718},
                      {"in": [30, 5807], "out": 37305},
                      {"in": [9, 48], "out": 63},
                      {"in": [1, 48], "out": 95},
                    ]

    def test_it(self):
        for case in self.cases:
            self.assertEqual(play(*case["in"])[1], case["out"])


if __name__ == '__main__':
    unittest.main()

# eof
