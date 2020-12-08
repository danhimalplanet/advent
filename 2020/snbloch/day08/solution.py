from collections import defaultdict

instructions = []
for line in open('input.txt', 'r'):
    line = line.strip().split()
    instructions.append((line[0], line[1]))

class intcodeComputer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator = 0
        self.position = 0
    def execute_instruction(self):
        if self.instructions[self.position][0] == 'nop':
            self.position += 1
        elif self.instructions[self.position][0] == 'acc':
            self.accumulator += int(self.instructions[self.position][1])
            self.position += 1
        elif self.instructions[self.position][0] == 'jmp':
            self.position += int(self.instructions[self.position][1])

def part1():
    computer = intcodeComputer(instructions)
    seen = set()
    while computer.position not in seen:
        seen.add(computer.position)
        computer.execute_instruction()
    print(computer.accumulator)

def part2():
    for i in range(len(instructions)):
        computer = intcodeComputer(instructions.copy())
        if computer.instructions[i][0] == 'nop':
            computer.instructions[i] = ('jmp', computer.instructions[i][1])
        elif computer.instructions[i][0] == 'jmp':
            computer.instructions[i] = ('nop', computer.instructions[i][1])
        seen = defaultdict(int)
        while computer.position < len(computer.instructions):
            seen[computer.position] += 1
            computer.execute_instruction()
            if max(seen.values()) > 1:
                break
        if computer.position >= len(computer.instructions):
            print(computer.accumulator)

if __name__ == '__main__':
    part1()
    part2()