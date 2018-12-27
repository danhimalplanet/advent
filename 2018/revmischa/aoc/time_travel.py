"""Time travel computer simulator."""
from collections import defaultdict
from typing import Dict, List, Tuple, Union
import time
import os

DEBUG = os.getenv('DEBUG', False)


RegVal = int
RegName = int
OpCodeInst = Union[int, str]
OpCodeT = Tuple[OpCodeInst, int, int, int]  # an instruction (day16)
Program = List[OpCodeT]
Regs = List[RegVal]


class OpCode:
    def __init__(self, op: OpCodeT):
        inst, a, b, c = op
        self.inst = inst
        self.a = a
        self.b = b
        self.c = c

    def exec_regs(self, regs: Regs) -> Regs:
        regs[self.c] = self.exec(regs)
        return regs

    def exec(self, regs: Regs) -> RegVal:
        raise NotImplementedError(f"not implemented: {self.inst}")

    def test(self, before_regs: Regs, after_regs: Regs) -> bool:
        """Check if executing this opcode on before_regs results in after_regs."""
        comp = TimeComputer(regs=before_regs)
        after_regs_comp = comp.exec(self)
        return after_regs_comp == after_regs

    @classmethod
    def decode(cls, op: OpCodeT) -> 'OpCode':
        """Given op with mnemonic, return appropriate op."""
        name_class_map = dict(
            addr=AddR,
            addi=AddI,
            mulr=MulR,
            muli=MulI,
            banr=BAnR,
            bani=BAnI,
            borr=BOrR,
            bori=BOrI,
            setr=SetR,
            seti=SetI,
            gtir=GTIR,
            gtri=GTRI,
            gtrr=GTRR,
            eqir=EqIR,
            eqri=EqRI,
            eqrr=EqRR,
        )
        op_cls = name_class_map.get(op[0])
        if not op_cls:
            raise Exception(f"Unknown opcode mnemonic {op[0]}")

        return op_cls(op)

    def __repr__(self):
        return f"{self.inst} {self.a} {self.b} {self.c}"


class AddR(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return regs[self.a] + regs[self.b]

class AddI(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return regs[self.a] + self.b

class MulR(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return regs[self.a] * regs[self.b]

class MulI(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return regs[self.a] * self.b

class BAnR(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return regs[self.a] & regs[self.b]

class BAnI(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return regs[self.a] & self.b

class BOrR(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return regs[self.a] | regs[self.b]

class BOrI(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return regs[self.a] | self.b

class SetR(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return regs[self.a]

class SetI(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return self.a

class GTIR(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return 1 if self.a > regs[self.b] else 0

class GTRI(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return 1 if regs[self.a] > self.b else 0

class GTRR(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        # print(f"checking if {regs[self.a]} > {regs[self.b]}")
        return 1 if regs[self.a] > regs[self.b] else 0

class EqIR(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        return 1 if self.a == regs[self.b] else 0

class EqRI(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        # print(f"checking if {regs[self.a]} == {self.b}")
        return 1 if regs[self.a] == self.b else 0

class EqRR(OpCode):
    def exec(self, regs: Regs) -> RegVal:
        # print(f"checking if {regs[self.a]} == {regs[self.b]}")
        return 1 if regs[self.a] == regs[self.b] else 0


ALL_OPCODES = [
    AddR, AddI,
    MulR, MulI,
    BAnR, BAnI,
    BOrR, BOrI,
    SetR, SetI,
    GTIR, GTRI, GTRR,
    EqIR, EqRI, EqRR,
]

Program = List[OpCode]

class TimeComputer:
    def __init__(self, program: Program = [], regs: Regs = None, pc_reg: int = None, reg_0=0):
        if regs:
            self.regs = regs[:]
        else:
            self.regs = [reg_0, 0, 0, 0, 0, 0]
        # self.regs: Dict[RegName, RegVal] = defaultdict(RegVal)

        self._pc = 0  # ip
        self.pc_reg = pc_reg  # what register is used for PC
        self.program = program  # instructions
        self._debug = DEBUG

    def debug(self, msg: str):
        if self._debug:
            print(msg)

    def __getitem__(self, reg: RegName) -> RegVal:
        if reg < 0 or reg >= len(self.regs):
            raise Exception(f"invalid register {reg}")
        return self.regs.get(reg, 0)

    def __setitem__(self, reg: RegName, val: RegVal):
        if reg < 0 or reg >= len(self.regs):
            raise Exception(f"invalid register {reg}")
        self.regs[reg] = val

    def exec(self, op: OpCode):
        """Execute one instruction."""
        return op.exec_regs(self.regs)

    def get_pc(self) -> int:
        if self.pc_reg is not None:
            return self.regs[self.pc_reg]
        else:
            return self._pc

    def inc_pc(self):
        if self.pc_reg is not None:
            self.regs[self.pc_reg] += 1
        else:
            self._pc += 1

    def cur_inst(self) -> OpCodeT:
        if self.pc_reg is not None:
            return self.program[self.regs[self.pc_reg]]
        else:
            return self.program[self._pc]

    def run(self, inst_mapping: Dict[int, OpCode] = None):
        while True:
            i: OpCodeT = self.cur_inst()

            if inst_mapping:
                # decode instruction from mapping (day16)
                opcodeCls = inst_mapping[i[0]]
                op = opcodeCls(i)
                self.exec(op)
            else:
                # decode instruction from asm (day19)
                op = OpCode.decode(i)
                self.debug(f"\n> {op} -\t {self.regs}")
                self.regs = self.exec(op)
                self.debug(f"ip={self.get_pc()}        -\t {self.regs}")
                if self._debug:
                    time.sleep(0.2)

            # increment pc
            self.inc_pc()

            if self.get_pc() >= len(self.program):
                # invalid program location
                print("HALTED")
                return
