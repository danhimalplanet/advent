import os
import sys
from typing import List


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, "..", ".."))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer
from pprint import pprint  # noqa: F401
from shapely.geometry import Point, LineString
from shapely.ops import split

class Day3(Computer):
    pwd: str = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.w1: List[str] = structure[0]
        self.w2: List[str] = structure[1]

    @classmethod
    def parse_input(cls, input_str: str):
        (w1s, w2s) = input_str.split("\n")
        return w1s.split(","), w2s.split(",")

    def run_part1(self):
        g1 = self.make_geom(self.w1)
        g2 = self.make_geom(self.w2)
        intshape = g1.intersection(g2)
        min_dist = 1000000000
        for point in intshape:
            if point.x == 0 and point.y == 0:
                continue
            # get distance at intersection
            dist = self.manhattan_dist(point.x, point.y)
            if dist < min_dist:
                min_dist = dist
        return min_dist

    def make_geom(self, ws: List[str]):
        x = 0
        y = 0
        points = [Point(0, 0)]
        for wd in ws:
            # get coords of next wire segment
            direction, magnitude = wd[0], int(wd[1:])
            if direction == "U":
                y += magnitude
            elif direction == "D":
                y -= magnitude
            elif direction == "R":
                x += magnitude
            elif direction == "L":
                x -= magnitude
            points.append(Point(x, y))

        geom = LineString(points)
        return geom

    def manhattan_dist(self, x: int, y: int):
        # distance from origin
        return abs(x) + abs(y)

    def run_part2(self):
        g1 = self.make_geom(self.w1)
        g2 = self.make_geom(self.w2)
        intshape = g1.intersection(g2)
        min_steps = 1000000000
        for point in intshape:
            if point.x == 0 and point.y == 0:
                continue
            # split the lines at the intersection and take the lengths
            s1 = split(g1, point)
            s2 = split(g2, point)
            steps = s1[0].length + s2[0].length
            if steps < min_steps:
                min_steps = steps
        return min_steps


if __name__ == "__main__":
    print(Day3.part1_result(debug=False))
    print(Day3.part2_result(debug=False))
