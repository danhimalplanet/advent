#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from solution import part1, part2


class TestPart1(unittest.TestCase):
    def setUp(self):
        self.input = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        self.output = 12

    def test_it(self):
        self.assertEqual(part1(self.input), self.output)


class TestPart2(unittest.TestCase):
    def setUp(self):
        self.input = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
        self.output = "fgij"

    def test_it(self):
        self.assertEqual(part2(self.input), self.output)



if __name__ == '__main__':
    unittest.main()

# eof
