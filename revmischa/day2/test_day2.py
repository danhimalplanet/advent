import unittest
from day2 import checksum_diff, checksum_div, spreadsheet_str_to_2d_array


class Day2TestCase(unittest.TestCase):
    def test_diff_checksums(self):
        input_str = """5 1 9 5
7 5 3
2 4 6 8"""
        spreadsheet = spreadsheet_str_to_2d_array(input_str)
        self.assertEqual(checksum_diff(spreadsheet), 18, "Incorrect checksum")

    def test_div_checksums(self):
        input_str = """5 9 2 8
9 4 7 3
3 8 6 5"""
        spreadsheet = spreadsheet_str_to_2d_array(input_str)
        self.assertEqual(checksum_div(spreadsheet), 9, "Incorrect checksum")
