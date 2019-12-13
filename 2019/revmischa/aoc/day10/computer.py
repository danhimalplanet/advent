import os
import sys

PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401
from typing import Iterable, Tuple, Optional

Asteroid = Tuple[int, int]


class Day10(Computer):
    pwd: str = PWD
    mat: Iterable[Iterable[int]]
    ass: Iterable[Asteroid]

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.input = structure
        mat, ass = structure
        self.mat = mat
        self.ass = ass

    @classmethod
    def parse_input(cls, input_str: str):
        y = 0
        mat = []
        ass = []
        for line in input_str.split("\n"):
            row = []
            x = 0
            for c in line:
                if c == "#":
                    row.append("#")
                    ass.append((x, 4-y))
                else:
                    row.append(" ")
                x += 1
            y += 1
            mat.append(row)
        # mat.reverse()
        return (mat, ass)

    def run_part1(self):
        # print(self.mat)
        # print(self.ass)
        # for each asteroid, calculate number of other visible asteroids
        best = 0
        self.print_mat()
        for ass in self.ass:
            visible = self.calc_visible(ass)
            x, y = ass
            self.mat[4-y][x] = visible
            if visible > best:
                best = visible

        self.print_mat()
        return best

    def print_mat(self):
        print('')
        for row in self.mat:
            for col in row:
                print(col, end='')
            print('')

    def calc_visible(self, ass: Asteroid) -> int:
        ax, ay = ass
        visible_count = 0
        for target in self.ass:
            if target == ass:
                continue

            bx, by = target
            intersected = False

            # get slope and y offset between ass and target
            slope: float = 0
            if bx - ax == 0:
                slope = 0.0
            else:
                slope = (by - ay) / (bx - ax)
            # b = y - slope * x
            offset = by - slope * bx
            # print(f"{ass} to {target}, slope={slope} offset={offset}")

            # check every other asteroid to see if it is in between and on the line between ass and target
            for other in self.ass:
                if other == ass or other == target:
                    continue

                # check if other point is on the line
                ox, oy = other
                if ox == 4 and oy == 1 and ass == (4,2) and target==(4,0):
                    import ipdb; ipdb.set_trace()
                yval = ox * slope + offset
                if not yval.is_integer():
                    continue
                yval = int(yval)
                if oy == yval:
                    # on the line
                    # does other live between ass and target?
                    if bx >= ax and (ox > bx or ox < ax):
                        continue
                    elif bx <= ax and (ox < bx or ox > ax):
                        continue
                    if by >= ay and (oy > by or oy < ay):
                        continue
                    elif by <= ay and (oy < by or oy > ay):
                        continue
                    # print(f"{other} is between {ass} and {target}")
                    intersected = True
                    break
                elif ox == ax == bx:
                    # same x coords
                    if ay < by and (oy > ay and oy < by):
                        # print(f"(x) {other} is between {ass} and {target}")
                        intersected = True
                    if ay > by and (oy < ay and oy > by):
                        # print(f"(x) {other} is between {ass} and {target}")
                        intersected = True

            if not intersected:
                # print(f"{ass} can see {target}")
                visible_count += 1

            # continue

            # # step through each integer x and y values between ass and other
            # xstep = 1 if bx > ax else -1
            # ystep = 1 if by > ay else -1
            # for x in range(ax, bx, xstep):
            #     y = slope * float(x) + offset
            #     print(x, y)
            #     if not y.is_integer():
            #         continue
            #     # does an asteroid exist at this crossing point?
            #     found = self.find_asteroid(int(x), int(y))
            #     if found and not (found[0] == bx and found[1] == by):
            #         continue
            #     # print("found intersection", found)
            # for y in range(ay, by, ystep):
            #     x = (y - offset) / slope
            #     print(x, y)
            #     if not x.is_integer():
            #         continue
            #     found = self.find_asteroid(int(x), int(y))
            #     if found and not (found[0] == bx and found[1] == by):
            #         continue
            #     # print("found intersection", found)
            # visible_count += 1

        return visible_count

    def find_asteroid(self, x, y) -> Optional[Asteroid]:
        matches = [a for a in self.ass if int(a[0]) == x and int(a[1]) == y]
        return matches[0] if matches else None

    def run_part2(self):
        return 0


if __name__ == "__main__":
    print(Day10.part1_result(debug=False))
    print(Day10.part2_result(debug=False))
