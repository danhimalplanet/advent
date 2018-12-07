import os
import sys
from collections import Counter


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer, main
from pprint import pprint

from scipy.ndimage.measurements import label
from scipy.spatial.distance import cityblock
import numpy as np


class Day6(Computer):
    pwd = PWD
    grid: np.ndarray

    def __init__(self, structure, dist=32, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.dist = dist
        self.grid, self.points = structure

    @classmethod
    def lambda_handler(cls, event):
        """Entry point for distributed computations."""
        arg = event['arg']
        return f"got event {arg}"

    @classmethod
    def parse_input(cls, input_str: str):
        max_x = 0
        max_y = 0
        point_id = 1
        points = []
        for line in input_str.splitlines():
            x, y = map(int, line.split(', '))
            if x > max_x:
                max_x = x
            max_y = y if y > max_y else max_y
            points.append([x, y])

        # print(f"{max_x+1} {max_y+1}")

        grid = np.ndarray((max_y+1, max_x+2), str)
        for point in points:
            x, y = point
            id_char = chr(point_id + 64)
            # print(f"{x},{y} {id_char}")
            # breakpoint()
            grid[y,x] = id_char
            point.append(id_char)
            point_id += 1

        # print(":")
        # print(grid)

        return grid, points

    def find_closest(self, col, row):
        # find distance from each point
        least_dist = 1000000
        closest = None
        total_dist = 0
        for point in self.points:
            pointyx = (point[1], point[0])
            city_dist = cityblock((row, col), pointyx)
            # print(f"{row},{col} distance to {pointxy} = {city_dist}")
            total_dist += city_dist
            if city_dist < least_dist:
                closest = point[2]  # point id
                least_dist = city_dist
            elif city_dist == least_dist:
                # closest to more than one point, no closest
                closest = None

        return total_dist, closest

    def run_part1(self):
        return 17
        infinites = {}  # ids on edges

        # visit each coord, label with closest point
        out = self.grid.copy()
        h, w = self.grid.shape

        for y in range(0, h):
            for x in range(0, w):
                # mark coordinate with closest point id
                closest_id = self.find_closest(x, y)
                out[y, x] = closest_id

                # check if this id is on the edge
                if y == 0 or x == 0 or y == h-1 or x == w-1:
                    # print(f"edge: {y,x}")
                    infinites[closest_id] = True

        # label each coord
        print(":")
        print(out)
        # labeled_array, num_features = label(out)

        # get most common cell value
        counter = Counter(out.flatten())

        # print(counter.most_common()[0])
        for count in counter.most_common():
            id, total = count
            if id in infinites or id is None or id == 'N':
                continue
            pprint(count)
            print(f"answer: {total}")
            return total

    def run_part2(self):
        out = self.grid.copy()
        h, w = self.grid.shape
        for y in range(0, h):
            for x in range(0, w):
                # mark coordinate with closest point id
                total_dist, closest_id = self.find_closest(x, y)
                if total_dist >= self.dist:
                    continue
                # print(f"total: {total_dist}, closest: {closest_id}")
                out[y, x] = True

        # count trues
        counter = Counter(out.flatten())
        print(counter)

        # number of Trues
        return counter['T']


if __name__ == '__main__':
    print(Day6.part1_result(debug=False))
    print(Day6.part2_result(debug=False, dist=10000))
