"""Common routines for solution computers.

Used day7 onwards.
"""
from abc import ABC, abstractmethod  # abstract base class
import re
import os


class Computer(ABC):
    """Base computer class.

    Handles parsing puzzle imports and defines protocol for computing part I and part II answers.
    """
    pwd = None

    @classmethod
    def part1_result(cls, *args, **kwargs):
        """Return part one answer."""
        comp = cls.new_from_puzzle_input(*args, **kwargs)
        return comp.run_part1()

    @classmethod
    def part2_result(cls, *args, **kwargs):
        """Return part two answer."""
        comp = cls.new_from_puzzle_input(*args, **kwargs)
        return comp.run_part2()

    @classmethod
    def new_from_puzzle_input(cls, *args, **kwargs):
        """Parse puzzle input string and construct computer.

        If input_ is not specified, read from input.
        """
        if not args:
            input_path = os.path.join(cls.pwd, "input") if cls.pwd else "input"
            with open(input_path, 'r') as input_file:
                args = [input_file.read()]
        parsed = cls.parse_input(*args, **kwargs)
        return cls(parsed, *args, **kwargs)

    @classmethod
    def parse_input(cls, input_str: str):
        """Convert input to python data structure.

        By default converts a list of ints.
        """
        parsed = list(
            map(
                int,
                filter(lambda n: n is not None and n is not "",
                       re.split(r"\s+", input_str))
            )
        )
        return parsed

    def __init__(self, *args, **kwargs):
        super().__init__()

    @abstractmethod
    def run_part1(self):
        pass

    @abstractmethod
    def run_part2(self):
        pass

def main(computer_cls: Computer, puzzle_input: str=None, *args, **kwargs):
    computer = computer_cls.new_from_puzzle_input(puzzle_input, *args, **kwargs)
    answer_1 = computer.run_part1()
    print(f'Part I Answer: {answer_1}')
    computer = computer_cls.new_from_puzzle_input(puzzle_input, *args, **kwargs)
    answer_2 = computer.run_part2()
    print(f'Part II Answer: {answer_2}')
