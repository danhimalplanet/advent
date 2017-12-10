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
    def part1_result(cls, input_str: str):
        """Return part one answer."""
        comp = cls.new_from_puzzle_input(input_str)
        return comp.run_part1()

    @classmethod
    def part2_result(cls, input_str: str):
        """Return part two answer."""
        comp = cls.new_from_puzzle_input(input_str)
        return comp.run_part2()

    @classmethod
    def new_from_puzzle_input(cls, input_str: str):
        """Parse puzzle input string and construct computer.

        If input_ is not specified, read from input.txt.
        """
        if not input_str:
            input_path = os.path.join(cls.pwd, "input.txt") if cls.pwd else "input.txt"
            with open(input_path, 'r') as input_file:
                input_str = input_file.read()
        parsed = cls.parse_input(input_str)
        return cls(parsed)

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

    def __init__(self, structure):
        super().__init__()

    @abstractmethod
    def run_part1(self):
        pass

    @abstractmethod
    def run_part2(self):
        pass
