import re
from typing import List
from pprint import pprint

BlockList = List[int]
BlockState = str

class Memory:
    @classmethod
    def new_from_puzzle_input(cls, input_: str):
        """Parse puzzle input string into python data structure."""
        parsed = list(
            map(int, 
                filter(lambda n: n is not None and n is not "",
                    re.split(r"\s+", input_)
                )
            )
        )
        return cls(parsed)

    def __init__(self, blocks: BlockList):
        self.blocks = blocks
        self.previous_states: List[BlockState] = list()

    def run_part1(self):
        cycle = 0
        done = False
        while not done:
            self.balance()
            cycle += 1
            done = self.seen_state(self.blocks)

        return cycle

    def run_part2(self):
        self.run_part1()
        self.previous_states = list(str(self.blocks))
        return self.run_part1()

        cycle = 0
        while not self.seen_state(self.blocks):
            self.balance()
            cycle += 1

        return cycle

    def seen_state(self, blocks: BlockList) -> bool:
        return str(blocks) in self.previous_states

    def balance(self):
        # find largest
        max_ = max(self.blocks)
        # index of first largest
        max_idx = self.blocks.index(max_)

        # save history
        self.previous_states.append(str(self.blocks))

        new_blocks: BlockList = list(self.blocks)
        new_blocks[max_idx] = 0  # steal all blocks from largest

        # redistribute
        i = max_idx + 1
        for j in range(0, max_):
            i %= len(new_blocks)  # wrap if necessary
            new_blocks[i] += 1
            i += 1

        self.blocks = new_blocks


if __name__ == '__main__':
    input_ = "14    0   15  12  11  11  3   5   1   6   8   4   9   1   8   4"
    computer = Memory.new_from_puzzle_input(input_)
    answer_1 = computer.run_part1()
    print(f'Part I Answer: {answer_1}')
    answer_2 = computer.run_part2()
    print(f'Part II Answer: {answer_2}')
