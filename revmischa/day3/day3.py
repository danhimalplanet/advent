import re
import numpy as np
import math

class Board():
    def __init__(self, starting_loc, use_sum=False):
        self.starting_loc = starting_loc
        self.dim = math.ceil(math.sqrt(self.starting_loc))
        self.use_sum = use_sum

    def distance(self):
        midpoint = int(self.dim / 2)
        (x, y) = self.loc_coords()

        dist_x = abs(x - midpoint)
        dist_y = abs(y - midpoint)
        return dist_x + dist_y

    def loc_coords(self, target=0):
        # board shape is ceil(√loc) w/h
        w = self.dim + 1
        h = self.dim + 1
        grid = np.zeros(shape=(w, h), dtype=int)

        midpoint = int(self.dim / 2)
        x = midpoint
        y = midpoint

        direction_changes = 0
        direction = 0
        cur = 0
        stride = 0
        stride_cur = 0  # progress on current stride
        val = 1
        for i in range(1, self.starting_loc+1):
            if i == 1:
                grid[y][x] = 1
                continue

            # count
            stride_cur += 1

            # place
            if direction == 0:  # right
                x += 1
            elif direction == 1:  # up
                y -= 1
            elif direction == 2:  # left
                x -= 1
            elif direction == 3:  # down
                y += 1

            val = i

            # print(grid)
            if self.use_sum:
                r_l = max(0, x-1)
                r_r = min(w, x+2)
                r_t = max(0, y-1)
                r_b = min(h, y+2)
                region = grid[r_t:r_b, r_l:r_r]
                # print(f"REGION {x,y} {r_l}:{r_r}, {r_t}:{r_b}")
                # print(region)
                # print("SUM: " + str(np.sum(region)))
                val = np.sum(region)

                if target and val > target:
                    return val

            if x >= w:
                w = x
                grid.reshape((w+1, h))
            if y >= h:
                h = y
                grid.reshape((w, h+1))

            grid[y][x] = val

            # check if we've gone far enough in this direction
            stride = math.ceil(math.sqrt(i+1)) - 1

            if stride_cur >= stride:
                direction = (direction + 1) % 4
                stride_cur = 0
            # print(grid)

        if self.use_sum:
            return val

        # print(f"Location of {self.starting_loc} is {{{x},{y}}}")
        return (x, y)


if __name__ == '__main__':
    board = Board(starting_loc=265149)
    print(f"Distance: {board.distance()}")
    board = Board(starting_loc=10000000, use_sum=True)
    print(f"Largest: {board.loc_coords(target=265149)}")