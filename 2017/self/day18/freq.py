#!/usr/bin/env python

import os.path
import sys


def val(regs, maybereg):
    if maybereg in regs:
        return regs[maybereg]

    return int(maybereg, 10)


def one(instructions):
    jumpout = len(instructions)
    regs = {}
    freqs = []

    pc = 0

    while True:
        ins = instructions[pc]
        if ins[1].isalpha() and ins[1] not in regs:
            regs[ins[1]] = 0
        if len(ins) == 3 and ins[2].isalpha() and ins[2] not in regs:
            regs[ins[2]] = 0

        if ins[0] == "set":
            regs[ins[1]] = val(regs, ins[2])
            pc += 1
        elif ins[0] == "add":
            regs[ins[1]] += val(regs, ins[2])
            pc += 1
        elif ins[0] == "mul":
            regs[ins[1]] *= val(regs, ins[2])
            pc += 1
        elif ins[0] == "mod":
            regs[ins[1]] %= val(regs, ins[2])
            pc += 1
        elif ins[0] == "snd":
            freqs.append(regs[ins[1]])
            pc += 1
        elif ins[0] == "rcv":
            if regs[ins[1]] != 0:
                regs[ins[1]] = freqs[-1]
            pc += 1
            return freqs[-1]
        elif ins[0] == "jgz":
            if regs[ins[1]] > 0:
                j = val(regs, ins[2])
                pc += j
                if pc < 0 or pc >= jumpout:
                    return
            else:
                pc += 1


def main(args):
    insn = [line.strip().split(" ") for line in open(args[0]).readlines()]
    print(one(insn[:]))


if __name__ == "__main__":
    main(sys.argv[1:])

# eof
