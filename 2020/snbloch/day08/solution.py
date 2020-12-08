from collections import defaultdict

class intcodeComputer:
    def __init__(self, filename):
        self.filename = filename
        self.instructions = []
        for line in open(filename, 'r'):
            line = line.strip().split()
            self.instructions.append((line[0], line[1]))
        self.position = 0
        self.accumulator = 0
    def execute_instruction(self):
        if self.instructions[self.position][0] == 'nop':
            self.position += 1
        elif self.instructions[self.position][0] == 'acc':
            self.accumulator += int(self.instructions[self.position][1])
            self.position += 1
        elif self.instructions[self.position][0] == 'jmp':
            self.position += int(self.instructions[self.position][1])
    def reset(self):
        self.instructions = []
        for line in open(self.filename, 'r'):
            line = line.strip().split()
            self.instructions.append((line[0], line[1]))
        self.position = 0
        self.accumulator = 0

def part1():
    computer = intcodeComputer('input.txt')
    seen = set()
    while computer.position not in seen:
        seen.add(computer.position)
        computer.execute_instruction()
    print(computer.accumulator)

def part2():
    computer = intcodeComputer('input.txt')
    counter = 0
    for i in computer.instructions:
        if i[0] == 'nop':
            computer.instructions[counter] = ('jmp', computer.instructions[counter][1])
        elif i[0] == 'jmp':
            computer.instructions[counter] = ('nop', computer.instructions[counter][1])
        seen = defaultdict(int)
        while computer.position < len(computer.instructions):
            seen[computer.position] += 1
            computer.execute_instruction()
            if max(seen.values()) > 1:
                computer.reset()
                counter += 1
                break
    print(computer.accumulator)

if __name__ == '__main__':
    part1()
    part2()