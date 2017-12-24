import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint
import numpy as np
from typing import List
from enum import Enum, unique

@unique
class Direction(Enum):
    up = 0
    right = 1
    down = 2
    left = 3

    def turn_right(self):
        n = self.value + 1
        if n > 3:
            n = 0
        return Direction(n)

    def turn_left(self):
        n = self.value - 1
        if n < 0:
            n = 3
        return Direction(n)

@unique
class NodeState(Enum):
    clean = 0
    weakened = 1
    infected = 2
    flagged = 3

    def next_state(self):
        n = self.value + 1
        if n > 3:
            n = 0
        return NodeState(n)

Row = List[NodeState]
Grid = List[Row]


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure: Grid, rounds: int=10000, **kwargs) -> None:
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.rounds = rounds
        self.infected_count = 0

        # init matrix
        self.mat: np.matrix = np.matrix(structure, dtype=int)
        self.w: int = self.mat.shape[1]
        self.h: int = self.mat.shape[0]
        self.r: int = int(self.h / 2)
        self.c: int = int(self.w / 2)
        self.direction: Direction = Direction.up

    @classmethod
    def parse_input(cls, input_str: str) -> Grid:
        lines = input_str.split('\n')
        grid: Grid = []
        for line in lines:
            row: Row = []
            for c in line:
                infected: NodeState = NodeState.infected.value if c == '#' else NodeState.clean.value
                row.append(infected)
            grid.append(row)
        return grid

    def iterate_part1(self) -> None:
        self.debug("----")
        infected: bool = self.mat[self.r, self.c]
        self.debug(f"Infected: {infected}, cur direction: {self.direction}, location: [{self.c}, {self.r}]")
        if infected:
            self.direction = self.direction.turn_right()
        else:
            # infecting
            self.infected_count += 1
            self.direction = self.direction.turn_left()
        self.debug(f"Infected: {infected}, new direction: {self.direction}")
        # toggle infected
        self.mat[self.r, self.c] = not infected
        # move
        self.move()
        self.debug(f"new location: [{self.c}, {self.r}]")
        self.debug(self.mat)

    def iterate_part2(self) -> None:
        self.debug("----")
        state: NodeState = NodeState(self.mat[self.r, self.c])
        self.debug(f"state: {state}, cur direction: {self.direction}, location: [{self.c}, {self.r}]")
        if state is NodeState.clean:
            self.direction = self.direction.turn_left()
        elif state is NodeState.weakened:
            pass
        elif state is NodeState.infected:
            self.direction = self.direction.turn_right()
        elif state is NodeState.flagged:
            # u-turn
            self.direction = self.direction.turn_right().turn_right()
        else:
            raise Exception(f"unknown state: {state}")
        self.debug(f"new direction: {self.direction}")
        # toggle infected
        next_state = state.next_state()
        if next_state is NodeState.infected:
            self.infected_count += 1
        self.mat[self.r, self.c] = next_state.value
        # move
        self.move()
        self.debug(f"new location: [{self.c}, {self.r}]")
        self.debug(self.mat)

    def move(self):
        if self.direction is Direction.up:
            self.r -= 1
        elif self.direction is Direction.right:
            self.c += 1
        elif self.direction is Direction.down:
            self.r += 1
        elif self.direction is Direction.left:
            self.c -= 1
        else:
            raise Exception("i messed up")

        if self.r < 0 or self.r >= self.h:
            new_mat = np.zeros((self.h + 2, self.w))
            new_mat[1:self.h+1, 0:self.w] = self.mat
            self.h += 2
            self.r += 1
            self.mat = new_mat
        if self.c < 0 or self.c >= self.w:
            new_mat = np.zeros((self.h, self.w + 2))
            new_mat[0:self.h, 1:self.w+1] = self.mat
            self.w += 2
            self.c += 1
            self.mat = new_mat

    def run_part1(self) -> int:
        for _ in range(self.rounds):
            self.iterate_part1()
        return self.infected_count

    def run_part2(self) -> int:
        for _ in range(self.rounds):
            self.iterate_part2()
        return self.infected_count


if __name__ == '__main__':
    print(DayN.part1_result(debug=False))
    print(DayN.part2_result(debug=False, rounds=10000000))
