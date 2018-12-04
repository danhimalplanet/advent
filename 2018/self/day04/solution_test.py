#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join
import unittest

from solution import part1, part2


class TestPart1(unittest.TestCase):
    def setUp(self):
        self.infp = open(join("resources", "test.txt"))
        self.input = [line.strip() for line in self.infp]
        self.output = 240

    def tearDown(self):
        self.infp.close()

    def test_it(self):
        _, _, wanted = part1(self.input)
        self.assertEqual(wanted, self.output)


class TestPart2(unittest.TestCase):
    def setUp(self):
        self.infp = open(join("resources", "test.txt"))
        self.input = [line.strip() for line in self.infp]
        self.output = 4455

    def tearDown(self):
        self.infp.close()

    def test_it(self):
        guards, sleeptime, _ = part1(self.input)
        self.assertEqual(part2(guards, sleeptime), self.output)



if __name__ == '__main__':
    unittest.main()

# eof
