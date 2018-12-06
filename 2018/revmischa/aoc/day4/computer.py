import datetime
import os
import sys
from collections import Counter
from dataclasses import dataclass, field
from typing import Dict, List

from dateutil import parser


PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from aoc.computer import Computer, main
from pprint import pprint

@dataclass
class Guard:
    id: int
    min_asleep: List[int] = field(default_factory=list)
    total_min_asleep: int = 0


class Day4(Computer):
    pwd = PWD

    def __init__(self, structure, **kwargs):
        """Construct solver with puzzle input."""
        super().__init__(structure, **kwargs)
        self.input = structure

    @classmethod
    def lambda_handler(cls, event):
        """Entry point for distributed computations."""
        arg = event['arg']
        return f"got event {arg}"

    @classmethod
    def parse_input(cls, input_str: str):
        cur_guard: Guard = None
        guard_sleep_start: datetime.datetime = None
        guards: Dict[int, Guard] = dict()

        for line in input_str.splitlines():
            stime, gid, action = cls.parse_line(line)
            # print(f"{stime} {gid} {action}")
            if action == 'begin':
                cur_guard = guards[gid] if gid in guards else Guard(id=gid)
                guards[gid] = cur_guard
            elif action == 'sleep':
                guard_sleep_start = stime
            elif action == 'wake':
                min_asleep = stime - guard_sleep_start
                min_start = guard_sleep_start.minute
                min_end = stime.minute
                cur_guard.min_asleep.extend(range(min_start, min_end))
                # print(f"--- {min_start} x {min_end}")
                # print(f"{cur_guard} min asleep: {min_asleep.total_seconds() / 60}")
                cur_guard.total_min_asleep += min_asleep.total_seconds() / 60

        return guards

    @classmethod
    def parse_line(cls, line):
        time_str = line[1:17]
        time_dt = parser.parse(time_str)
        act = line[19:]
        if act == 'falls asleep':
            return time_dt, None, 'sleep'
        elif act == 'wakes up':
            return time_dt, None, 'wake'
        else:
            gid = int(line[26:30])
            return time_dt, gid, 'begin'


    def run_part1(self):
        # guard with most min asleep
        guards = list(self.input.values())
        guards.sort(key=lambda g: g.total_min_asleep, reverse=True)
        guard = guards[0]

        # find minute most asleep
        min_counter = Counter(guard.min_asleep)
        top_min = None
        top_min_count = 0
        for minute, count in min_counter.items():
            if count > top_min_count:
                top_min = minute
                top_min_count = count

        return guard.id * top_min

    def run_part2(self):
        guards = list(self.input.values())

        the_min = None
        the_min_count = 0
        the_guard = None

        for guard in guards:
            min_counter = Counter(guard.min_asleep)
            common = min_counter.most_common()
            if not common:
                continue
            common = common[0]  # most common (min, count)

            if common[1] > the_min_count:
                the_min, the_min_count = common
                the_guard = guard

        return the_guard.id * the_min

if __name__ == '__main__':
    print(Day4.part1_result(debug=False))
    print(Day4.part2_result(debug=False))
