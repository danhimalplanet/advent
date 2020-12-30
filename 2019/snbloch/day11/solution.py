from collections import defaultdict

class IntCodeComputer:
    def __init__(self, program):
        self.program = defaultdict(int, enumerate(program))
        self.inputInstruction = []
        self.output = []
        self.firstParameterMode = None
        self.secondParameterMode = None
        self.thirdParameterMode = None
        self.position = 0
        self.currentInstruction = None
        self.relativeBase = 0
    def computeOperation(self, position, instruction):
        if instruction == 99:
            return None
        elif instruction == 1:
            if self.firstParameterMode == 0:
                firstParameter = self.program[self.program[position + 1]]
            elif self.firstParameterMode == 1:
                firstParameter = self.program[position + 1]
            elif self.firstParameterMode == 2:
                firstParameter = self.program[self.program[position + 1] + self.relativeBase]
            if self.secondParameterMode == 0:
                secondParameter = self.program[self.program[position + 2]]
            elif self.secondParameterMode == 1:
                secondParameter = self.program[position + 2]
            elif self.secondParameterMode == 2:
                secondParameter = self.program[self.program[position + 2] + self.relativeBase]
            if self.thirdParameterMode == 0:
                thirdParameter = self.program[position + 3]
            elif self.thirdParameterMode == 1:
                thirdParameter = position + 3
            elif self.thirdParameterMode == 2:
                thirdParameter = self.program[position + 3] + self.relativeBase
            self.program[thirdParameter] = firstParameter + secondParameter
            return position + 4
        elif instruction == 2:
            if self.firstParameterMode == 0:
                firstParameter = self.program[self.program[position + 1]]
            elif self.firstParameterMode == 1:
                firstParameter = self.program[position + 1]
            elif self.firstParameterMode == 2:
                firstParameter = self.program[self.program[position + 1] + self.relativeBase]
            if self.secondParameterMode == 0:
                secondParameter = self.program[self.program[position + 2]]
            elif self.secondParameterMode == 1:
                secondParameter = self.program[position + 2]
            elif self.secondParameterMode == 2:
                secondParameter = self.program[self.program[position + 2] + self.relativeBase]
            if self.thirdParameterMode == 0:
                thirdParameter = self.program[position + 3]
            elif self.thirdParameterMode == 1:
                thirdParameter = position + 3
            elif self.thirdParameterMode == 2:
                thirdParameter = self.program[position + 3] + self.relativeBase
            self.program[thirdParameter] = firstParameter * secondParameter
            return position + 4
        elif instruction == 3:
            if self.firstParameterMode == 0:
                firstParameter = self.program[position + 1]
            elif self.firstParameterMode == 1:
                firstParameter = position + 1
            elif self.firstParameterMode == 2:
                firstParameter = self.program[position + 1] + self.relativeBase
            self.program[firstParameter] = self.inputInstruction.pop(0)
            return position + 2
        elif instruction == 4:
            if self.firstParameterMode == 0:
                firstParameter = self.program[self.program[position + 1]]
            elif self.firstParameterMode == 1:
                firstParameter = self.program[position + 1]
            elif self.firstParameterMode == 2:
                firstParameter = self.program[self.program[position + 1] + self.relativeBase]
            self.output.append(firstParameter)
            return position + 2
        elif instruction == 5:
            if self.firstParameterMode == 0:
                firstParameter = self.program[self.program[position + 1]]
            elif self.firstParameterMode == 1:
                firstParameter = self.program[position + 1]
            elif self.firstParameterMode == 2:
                firstParameter = self.program[self.program[position + 1] + self.relativeBase]
            if self.secondParameterMode == 0:
                secondParameter = self.program[self.program[position + 2]]
            elif self.secondParameterMode == 1:
                secondParameter = self.program[position + 2]
            elif self.secondParameterMode == 2:
                secondParameter = self.program[self.program[position + 2] + self.relativeBase]
            if firstParameter != 0:
                 return secondParameter
            else:
                return position + 3
        elif instruction == 6:
            if self.firstParameterMode == 0:
                firstParameter = self.program[self.program[position + 1]]
            elif self.firstParameterMode == 1:
                firstParameter = self.program[position + 1]
            elif self.firstParameterMode == 2:
                firstParameter = self.program[self.program[position + 1] + self.relativeBase]
            if self.secondParameterMode == 0:
                secondParameter = self.program[self.program[position + 2]]
            elif self.secondParameterMode == 1:
                secondParameter = self.program[position + 2]
            elif self.secondParameterMode == 2:
                secondParameter = self.program[self.program[position + 2] + self.relativeBase]
            if firstParameter == 0:
                return secondParameter
            else:
                return position + 3
        elif instruction == 7:
            if self.firstParameterMode == 0:
                firstParameter = self.program[self.program[position + 1]]
            elif self.firstParameterMode == 1:
                firstParameter = self.program[position + 1]
            elif self.firstParameterMode == 2:
                firstParameter = self.program[self.program[position + 1] + self.relativeBase]
            if self.secondParameterMode == 0:
                secondParameter = self.program[self.program[position + 2]]
            elif self.secondParameterMode == 1:
                secondParameter = self.program[position + 2]
            elif self.secondParameterMode == 2:
                secondParameter = self.program[self.program[position + 2] + self.relativeBase]
            if self.thirdParameterMode == 0:
                thirdParameter = self.program[position + 3]
            elif self.thirdParameterMode == 1:
                thirdParameter = position + 3
            elif self.thirdParameterMode == 2:
                thirdParameter = self.program[position + 3] + self.relativeBase
            if firstParameter < secondParameter:
                self.program[thirdParameter] = 1
            else:
                self.program[thirdParameter] = 0
            return position + 4
        elif instruction == 8:
            if self.firstParameterMode == 0:
                firstParameter = self.program[self.program[position + 1]]
            elif self.firstParameterMode == 1:
                firstParameter = self.program[position + 1]
            elif self.firstParameterMode == 2:
                firstParameter = self.program[self.program[position + 1] + self.relativeBase]
            if self.secondParameterMode == 0:
                secondParameter = self.program[self.program[position + 2]]
            elif self.secondParameterMode == 1:
                secondParameter = self.program[position + 2]
            if self.secondParameterMode == 2:
                secondParameter = self.program[self.program[position + 2] + self.relativeBase]
            if self.thirdParameterMode == 0:
                thirdParameter = self.program[position + 3]
            elif self.thirdParameterMode == 1:
                thirdParameter = position + 3
            elif self.thirdParameterMode == 2:
                thirdParameter = self.program[position + 3] + self.relativeBase
            if firstParameter == secondParameter:
                self.program[thirdParameter] = 1
            else:
                self.program[thirdParameter] = 0
            return position + 4
        elif instruction == 9:
            if self.firstParameterMode == 0:
                firstParameter = self.program[self.program[position + 1]]
            elif self.firstParameterMode == 1:
                firstParameter = self.program[position + 1]
            elif self.firstParameterMode == 2:
                firstParameter = self.program[self.program[position + 1] + self.relativeBase]
            self.relativeBase += firstParameter
            return position + 2
    def computeParameterModes(self, instruction):
        if len(str(instruction)) == 1 or len(str(instruction)) == 2:
            self.currentInstruction = instruction
            self.firstParameterMode = 0
            self.secondParameterMode = 0
            self.thirdParameterMode = 0
        elif len(str(instruction)) == 3:
            self.currentInstruction = int(str(instruction)[1:])
            self.firstParameterMode = int(str(instruction)[0])
            self.secondParameterMode = 0
            self.thirdParameterMode = 0
        elif len(str(instruction)) == 4:
            self.currentInstruction = int(str(instruction)[2:])
            self.firstParameterMode = int(str(instruction)[1])
            self.secondParameterMode = int(str(instruction)[0])
            self.thirdParameterMode = 0
        elif len(str(instruction)) == 5:
            self.currentInstruction = int(str(instruction)[3:])
            self.firstParameterMode = int(str(instruction)[2])
            self.secondParameterMode = int(str(instruction)[1])
            self.thirdParameterMode = int(str(instruction)[0])

def part1():
    panels = {}
    cur_x = 0
    cur_y = 0
    cur_dir = '^'
    puzzleInput = [3,8,1005,8,320,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,29,2,1005,1,10,1006,0,11,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,57,1,8,15,10,1006,0,79,1,6,3,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,90,2,103,18,10,1006,0,3,2,105,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,123,2,9,2,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,150,1,2,2,10,2,1009,6,10,1,1006,12,10,1006,0,81,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,187,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,209,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,231,1,1008,11,10,1,1001,4,10,2,1104,18,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,264,1,8,14,10,1006,0,36,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,293,1006,0,80,1006,0,68,101,1,9,9,1007,9,960,10,1005,10,15,99,109,642,104,0,104,1,21102,1,846914232732,1,21102,1,337,0,1105,1,441,21102,1,387512115980,1,21101,348,0,0,1106,0,441,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,209533824219,1,1,21102,1,395,0,1106,0,441,21101,0,21477985303,1,21102,406,1,0,1106,0,441,3,10,104,0,104,0,3,10,104,0,104,0,21101,868494234468,0,1,21101,429,0,0,1106,0,441,21102,838429471080,1,1,21102,1,440,0,1106,0,441,99,109,2,21201,-1,0,1,21101,0,40,2,21102,472,1,3,21101,0,462,0,1106,0,505,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,467,468,483,4,0,1001,467,1,467,108,4,467,10,1006,10,499,1102,1,0,467,109,-2,2106,0,0,0,109,4,2101,0,-1,504,1207,-3,0,10,1006,10,522,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21102,1,1,3,21102,541,1,0,1106,0,546,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,569,2207,-4,-2,10,1006,10,569,22102,1,-4,-4,1105,1,637,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,588,1,0,1105,1,546,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,607,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,629,21201,-1,0,1,21102,629,1,0,105,1,504,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
    computer = IntCodeComputer(puzzleInput)
    computer.inputInstruction.append(0)
    panels[(cur_x, cur_y)] = 0
    while computer.position is not None:
        if len(computer.output) < 2:
            computer.computeParameterModes(computer.program[computer.position])
            computer.position = computer.computeOperation(computer.position, computer.currentInstruction)
        else:
            panels[(cur_x, cur_y)] = computer.output[0]
            if computer.output[1] == 0:
                if cur_dir == '^':
                    cur_x -= 1
                    cur_dir = '<'
                elif cur_dir == '<':
                    cur_y -= 1
                    cur_dir = 'v'
                elif cur_dir == 'v':
                    cur_x += 1
                    cur_dir = '>'
                elif cur_dir == '>':
                    cur_y += 1
                    cur_dir = '^'
            elif computer.output[1] == 1:
                if cur_dir == '^':
                    cur_x += 1
                    cur_dir = '>'
                elif cur_dir == '>':
                    cur_y -= 1
                    cur_dir = 'v'
                elif cur_dir == 'v':
                    cur_x -= 1
                    cur_dir = '<'
                elif cur_dir == '<':
                    cur_y += 1
                    cur_dir = '^'
            computer.output = []
            if (cur_x, cur_y) not in panels:
                panels[(cur_x, cur_y)] = 0
            instruction = panels[(cur_x, cur_y)]
            computer.inputInstruction.append(instruction)
            computer.computeParameterModes(computer.program[computer.position])
            computer.position = computer.computeOperation(computer.position, computer.currentInstruction)
    print(len(panels))

def part2():
    panels = {}
    cur_x = 0
    cur_y = 0
    cur_dir = '^'
    puzzleInput = [3,8,1005,8,320,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,29,2,1005,1,10,1006,0,11,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,57,1,8,15,10,1006,0,79,1,6,3,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,90,2,103,18,10,1006,0,3,2,105,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,123,2,9,2,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,150,1,2,2,10,2,1009,6,10,1,1006,12,10,1006,0,81,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,187,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,209,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,231,1,1008,11,10,1,1001,4,10,2,1104,18,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,264,1,8,14,10,1006,0,36,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,293,1006,0,80,1006,0,68,101,1,9,9,1007,9,960,10,1005,10,15,99,109,642,104,0,104,1,21102,1,846914232732,1,21102,1,337,0,1105,1,441,21102,1,387512115980,1,21101,348,0,0,1106,0,441,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,209533824219,1,1,21102,1,395,0,1106,0,441,21101,0,21477985303,1,21102,406,1,0,1106,0,441,3,10,104,0,104,0,3,10,104,0,104,0,21101,868494234468,0,1,21101,429,0,0,1106,0,441,21102,838429471080,1,1,21102,1,440,0,1106,0,441,99,109,2,21201,-1,0,1,21101,0,40,2,21102,472,1,3,21101,0,462,0,1106,0,505,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,467,468,483,4,0,1001,467,1,467,108,4,467,10,1006,10,499,1102,1,0,467,109,-2,2106,0,0,0,109,4,2101,0,-1,504,1207,-3,0,10,1006,10,522,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21102,1,1,3,21102,541,1,0,1106,0,546,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,569,2207,-4,-2,10,1006,10,569,22102,1,-4,-4,1105,1,637,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,588,1,0,1105,1,546,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,607,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,629,21201,-1,0,1,21102,629,1,0,105,1,504,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
    computer = IntCodeComputer(puzzleInput)
    computer.inputInstruction.append(1)
    panels[(cur_x, cur_y)] = 1
    while computer.position is not None:
        if len(computer.output) < 2:
            computer.computeParameterModes(computer.program[computer.position])
            computer.position = computer.computeOperation(computer.position, computer.currentInstruction)
        else:
            panels[(cur_x, cur_y)] = computer.output[0]
            if computer.output[1] == 0:
                if cur_dir == '^':
                    cur_x -= 1
                    cur_dir = '<'
                elif cur_dir == '<':
                    cur_y += 1
                    cur_dir = 'v'
                elif cur_dir == 'v':
                    cur_x += 1
                    cur_dir = '>'
                elif cur_dir == '>':
                    cur_y -= 1
                    cur_dir = '^'
            elif computer.output[1] == 1:
                if cur_dir == '^':
                    cur_x += 1
                    cur_dir = '>'
                elif cur_dir == '>':
                    cur_y += 1
                    cur_dir = 'v'
                elif cur_dir == 'v':
                    cur_x -= 1
                    cur_dir = '<'
                elif cur_dir == '<':
                    cur_y -= 1
                    cur_dir = '^'
            computer.output = []
            if (cur_x, cur_y) not in panels:
                panels[(cur_x, cur_y)] = 0
            instruction = panels[(cur_x, cur_y)]
            computer.inputInstruction.append(instruction)
            computer.computeParameterModes(computer.program[computer.position])
            computer.position = computer.computeOperation(computer.position, computer.currentInstruction)
    max_x = 0
    max_y = 0
    for p in panels:
        if p[0] > max_x:
            max_x = p[0]
        if p[1] > max_y:
            max_y = p[1]
    grid = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            if (x,y) not in panels:
                row.append('.')
            elif panels[(x, y)] == 1:
                row.append('#')
            else:
                row.append('.')
        grid.append(row)
    for line in grid:
        print(''.join(line))

if __name__ == '__main__':
    part1()
    part2()