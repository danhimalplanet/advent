import io

def addr(before, instruction):
    C = foo

def part1():
    before = []
    instructions = []
    after = []
    with open('test.txt', 'r') as inputfile:
        for line in inputfile:
            if 'Before: ' in line:
                registers = []
                for i in line.strip().replace('Before: ', '').replace('[', '').replace(']', '').split(', '):
                    registers.append(int(i))
                before.append(registers)
            elif 'After: ' in line:
                registers = []
                for i in line.strip().replace('After: ', '').replace('[', '').replace(']', '').split(', '):
                    registers.append(int(i))
                after.append(registers)
            else:
                instruction = []
                for i in line.strip().split():
                    instruction.append(int(i))
                instructions.append(instruction)
    print before, instructions, after

if __name__ == '__main__':
    part1()
