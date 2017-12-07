import unittest
from dayN import Program


class DayNTestCase(unittest.TestCase):
    def test_jumps_recur(self):
        prog1 = Program(jumps_str="""0
3
0
1
-3
""")
        self.assertEqual(prog1.execute_recursively(), 5)

    def test_jumps_iter(self):
        prog1 = Program(jumps_str="""0
3
0
1
-3
""")
        self.assertEqual(prog1.execute_iteratively(), 5)
