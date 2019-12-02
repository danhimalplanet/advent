"""Common routines for solution computers."""
from abc import ABC, abstractmethod  # abstract base class
import re
import os
import json
from aoc import get_boto_session, current_day
from concurrent.futures import ThreadPoolExecutor
import logging
from typing import Dict, Optional

log = logging.getLogger(__name__)


class Computer(ABC):
    """Base computer class.

    Handles parsing puzzle imports and defines interface for computing part I and part II answers.
    """

    pwd: Optional[str] = None

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
    def new_from_puzzle_input(cls, input_=None, *args, **kwargs):
        """Parse puzzle input string and construct computer.

        If input_ is not specified, read from input.
        """
        if not input_:
            input_path = os.path.join(cls.pwd, "input") if cls.pwd else "input"
            with open(input_path, "r") as input_file:
                input_ = input_file.read()
        parsed = cls.parse_input(input_)
        return cls(parsed, *args, **kwargs)

    @classmethod
    def parse_input(cls, input_str: str):
        """Convert input to python data structure.

        By default converts a list of ints.
        """
        parsed = list(
            map(
                int,
                filter(
                    lambda n: n is not None and n != "", re.split(r"\s+", input_str)
                ),
            )
        )
        return parsed

    def serverless_map(self, job_count: int, *args):
        """Spawn `job_count` lambdas and call lambda_handler with args[j]."""
        if len(args) != job_count:
            raise Exception(
                f"arg length {len(args)} doesn't match job count {job_count}"
            )

        with ThreadPoolExecutor(max_workers=10) as executor:
            futs = []
            for j in range(job_count):
                arg = args[j]
                log.info(f"Spawning task {arg}")
                futs.append(
                    executor.submit(
                        lambda: self.invoke_lambda(
                            day=current_day, payload=dict(arg=arg)
                        )
                    )
                )

        results = [fut.result() for fut in futs]
        return results

    def invoke_lambda(self, day: int, payload: Dict):
        """Invoke lambda for day with payload and return result."""
        lmbda = get_boto_session().client("lambda")
        res = lmbda.invoke(
            FunctionName="aoc-dev-aoc",
            InvocationType="RequestResponse",  # synchronous
            Payload=json.dumps(dict(day=current_day, **payload,)),
        )
        res = json.loads(res["Payload"].read())
        if "errorMessage" in res:
            # failed to execute
            raise Exception(res)
        return res["result"]

    def __init__(self, *args, debug=True, **kwargs):
        super().__init__()
        self._debug = debug

    def debug(self, msg: str):
        if self._debug:
            print(msg)

    @abstractmethod
    def run_part1(self):
        pass

    @abstractmethod
    def run_part2(self):
        pass


def main(computer_cls: Computer, puzzle_input: str = None, *args, **kwargs):
    computer = computer_cls.new_from_puzzle_input(puzzle_input, *args, **kwargs)
    answer_1 = computer.run_part1()
    print(f"Part I Answer: {answer_1}")
    computer = computer_cls.new_from_puzzle_input(puzzle_input, *args, **kwargs)
    answer_2 = computer.run_part2()
    print(f"Part II Answer: {answer_2}")
