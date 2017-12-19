import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.input = structure

    @classmethod
    def parse_input(cls, input_str: str):
        lines = input_str.split("\n")
        r = []
        for line in lines:
            r.append(list(line))
        return r

    def run_part1(self):
        grid = self.input
        collected = []

        y = 0
        # find start
        x = grid[0].index('|')

        last_dir = 'u'
        direction = 'd'

        done = False
        while not done:
            char = grid[y][x]
            # print(f"[{x},{y}] {char}  dir={direction}  last_dir={last_dir}")

            if char == '|' or char == '-':
                pass
            elif char == '+':
                # change direction
                if direction == 'u' or direction == 'd':
                    if x == 0 or grid[y][x - 1] == ' ':
                        direction = 'r'
                    else:
                        direction = 'l'
                elif direction == 'l' or direction == 'r':
                    if y == 0 or grid[y - 1][x] == ' ':
                        direction = 'd'
                    else:
                        direction = 'u'            
            elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                collected.append(char)
            elif char == ' ':
                # end?
                print("reached end")
                done = True
            else:
                raise Exception(f"unknown char {char}")

            if direction == 'd':
                y += 1
            elif direction == 'u':
                y -= 1
            elif direction == 'r':
                x += 1
            elif direction == 'l':
                x -= 1
            else:
                raise Exception(f"unknown direction {direction}")
        return ''.join(collected)

    def run_part2(self):
        return 0

if __name__ == '__main__':
    main(DayN)
