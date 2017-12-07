"""Common routines for solution computers.

Used day7 onwards.
"""
from abc import ABC, abstractmethod  # abstract base class
import re


class Computer(ABC):
    """Base computer class.

    Handles parsing puzzle imports and defines protocol for computing part I and part II answers.
    """
    @classmethod
    def new_from_puzzle_input(cls, input_: str=None):
        """Parse puzzle input string into python data structure and construct computer.

        If input_ is not specified, read from input.txt.
        """
        if not input_:
            with open("input.txt", 'r') as input_file:
                input_ = input_file.read()

        parsed = list(
            map(
                int,
                filter(lambda n: n is not None and n is not "",
                       re.split(r"\s+", input_))
            )
        )
        return cls(parsed)

    def __init__(self, structure):
        super().__init__()

    @abstractmethod
    def run_part1(self):
        pass

    @abstractmethod
    def run_part2(self):
        pass
