import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from typing import List, Tuple, Dict
from pprint import pprint
from collections import namedtuple
import re
import numpy as np

Direction = str
StateName = str
State = namedtuple('State', ['name', 'zero_write', 'zero_dir', 'zero_next_state',
                             'one_write', 'one_dir', 'one_next_state'])
StateMap = Dict[StateName, State]


STATE_DESC_REGEX = r"""In state (?P<name>[A-Z]):
  If the current value is 0:
    - Write the value (?P<zero_write>\d).
    - Move one slot to the (?P<zero_dir>(left|right)).
    - Continue with state (?P<zero_next_state>[A-Z]).
  If the current value is 1:
    - Write the value (?P<one_write>\d).
    - Move one slot to the (?P<one_dir>(left|right)).
    - Continue with state (?P<one_next_state>[A-Z])."""

class DayN(Computer):
    pwd = PWD

    def __init__(self, structure: StateMap, rounds):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.states: StateMap = structure
        self.current_state = self.states['A']
        self.rounds = rounds
        self.tape = np.zeros(shape=(rounds, 1), dtype=int)
        self.pos = int(rounds / 2)

    @classmethod
    def parse_input(cls, input_str: str):
        states: StateMap = {}
        # read state descs
        for match in re.finditer(STATE_DESC_REGEX, input_str):
            state = State(**match.groupdict())
            states[state.name] = state
        return states

    def tick(self):
        state = self.current_state
        cur_val: int = self.tape[self.pos]
        if cur_val == 0:
            self.tape[self.pos] = state.zero_write
            self.move(state.zero_dir)
            self.current_state = self.states[state.zero_next_state]
        elif cur_val == 1:
            self.tape[self.pos] = state.one_write
            self.move(state.one_dir)
            self.current_state = self.states[state.one_next_state]
            
    def move(self, direction: Direction):
        # move in direction
        if direction == 'left':
            self.pos -= 1
        elif direction == 'right':
            self.pos += 1
        else:
            raise Exception(f'unknown direction {direction}')

    def run_part1(self):
        for i in range(self.rounds):
            self.tick()
        return self.tape.sum()


if __name__ == '__main__':
    print(DayN.part1_result(rounds=12994925))

