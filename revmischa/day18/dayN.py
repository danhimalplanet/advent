import os
import sys
PWD = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.join(PWD, '..', '..'))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)

from revmischa import Computer, main
from pprint import pprint
from collections import defaultdict
from typing import Any, List
import asyncio


class DayN(Computer):
    pwd = PWD

    def __init__(self, structure, stop_on_recv=True, p=0, loop=None):
        """Construct solver with puzzle input."""
        super().__init__(structure)
        self.input = structure
        self.regs: List[tuple] = defaultdict(int)
        self.regs['p'] = p
        self.p = p
        self.pc = 0
        self.last_snd = 0
        self.recv = 0
        self.stop_on_recv = stop_on_recv
        self.q = asyncio.Queue(loop=loop)
        self.send_count = 0
        self.other_q = None

    def __getitem__(self, reg):
        if reg in self.regs:
            return self.regs[reg]
        return 0

    def __setitem__(self, reg, val):
        self.regs[reg] = val

    @classmethod
    def parse_input(cls, input_str: str):
        lines = input_str.split("\n")
        insts = []
        for line in lines:
            code = line.split(' ')
            op: str = code[0]
            reg: str = code[1]
            operand: Any = None
            if len(code) == 3:
                if code[2].isalpha():
                    operand = code[2]
                else:
                    operand = int(code[2])
            insts.append((op, reg, operand))
        return insts

    async def run(self):
        while self.pc < len(self.input):
            i = self.input[self.pc]
            (op, reg, operand) = i
            if type(operand) is str:
                operand = self[operand]

            # print(f"[{self.p}]  -  {i} reg: {reg}, val: {self[reg]}, operand: {operand}")

            if op == 'snd':
                await self.snd(reg)
            elif op == 'set':
                self[reg] = operand
            elif op == 'add':
                self[reg] = self[reg] + operand
            elif op == 'mul':
                self[reg] = self[reg] * operand
            elif op == 'mod':
                self[reg] = self[reg] % operand
            elif op == 'rcv':
                await self.rcv(reg)
                if self.stop_on_recv and self.last_snd != 0:
                    self.last_recv = self.last_snd
                    return
            elif op == 'jgz':
                v = self[reg]
                if v > 0:
                    self.pc += operand
                    continue
            else:
                print(f"Unknown op {op}")

            self.pc += 1

    async def rcv(self, reg):
        self[reg] = self.last_snd

    async def snd(self, reg):
        self.last_snd = self[reg]

    def run_part1(self):
        self.run()
        return self.last_snd

    def run_part2(self):
        pass


receiving = {1: False, 0: False}
class DeadlockException(Exception):
    pass

class Day18b(DayN):
    async def rcv(self, reg):
        # print(f"Receiving {reg}...")
        receiving[self.p] = True

        # print(f"[{self.p}] Receiving: {receiving}")
        print(f"[{self.p}] qsize: {self.q.qsize()} other: {self.other_q.qsize()}")

        if all(receiving.values()) and self.q.empty() and self.other_q.empty():
            raise DeadlockException()

        r = await self.q.get()
        print(f"Received {reg}={r}")
        receiving[self.p] = False
        self[reg] = r

    async def snd(self, operand):
        if operand.isalpha():
            operand = self[operand]
        print(f"[{self.p}] Sending {operand}, count = {self.send_count + 1}")
        await self.other_q.put(operand)
        self.send_count += 1


def run_part2(inp=None):
    loop = asyncio.get_event_loop()

    comp2_a = Day18b.new_from_puzzle_input(input_=inp, p=0, loop=loop)
    comp2_b = Day18b.new_from_puzzle_input(input_=inp, p=1, loop=loop)
    comp2_b.other_q = comp2_a.q
    comp2_a.other_q = comp2_b.q

    # agen = comp2_a.run()
    # bgen = comp2_b.run()

    async def exc(res):
        t1 = comp2_a.run()
        t2 = comp2_b.run()

        try:
            for t in asyncio.as_completed([t2, t1]):
                print(await t)
        except DeadlockException:
            print(f"Deadlock!")
            res.set_result(comp2_a.send_count)

    res = asyncio.Future()
    loop.run_until_complete(exc(res))
    return res.result()


if __name__ == '__main__':
    # comp1 = DayN.new_from_puzzle_input()
    # print(comp1.run_part1())
    print(run_part2())
