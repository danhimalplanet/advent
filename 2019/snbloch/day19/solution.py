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
    puzzleInput = [109,424,203,1,21101,11,0,0,1105,1,282,21102,1,18,0,1105,1,259,1201,1,0,221,203,1,21102,31,1,0,1106,0,282,21101,38,0,0,1106,0,259,21001,23,0,2,22102,1,1,3,21101,0,1,1,21102,57,1,0,1106,0,303,1202,1,1,222,20102,1,221,3,21002,221,1,2,21101,259,0,1,21102,80,1,0,1106,0,225,21101,0,51,2,21101,0,91,0,1106,0,303,1202,1,1,223,20101,0,222,4,21101,259,0,3,21102,225,1,2,21101,225,0,1,21101,118,0,0,1105,1,225,20102,1,222,3,21102,1,152,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1105,1,259,1202,1,1,223,20101,0,221,4,21002,222,1,3,21102,1,17,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,108,20207,1,223,2,21002,23,1,1,21102,1,-1,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,22101,0,-3,1,21202,-2,1,2,22102,1,-1,3,21101,250,0,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21102,1,343,0,1105,1,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21202,-4,1,1,21102,1,384,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2105,1,0]
    affected = 0
    for y in range(50):
        for x in range(50):
            computer = IntCodeComputer(puzzleInput)
            computer.inputInstruction.append(x)
            computer.inputInstruction.append(y)
            while len(computer.output) == 0:
                computer.computeParameterModes(computer.program[computer.position])
                computer.position = computer.computeOperation(computer.position, computer.currentInstruction)
            if computer.output[0] == 1:
                affected += 1
    print(affected)

def part2():
    puzzleInput = [109,424,203,1,21101,11,0,0,1105,1,282,21102,1,18,0,1105,1,259,1201,1,0,221,203,1,21102,31,1,0,1106,0,282,21101,38,0,0,1106,0,259,21001,23,0,2,22102,1,1,3,21101,0,1,1,21102,57,1,0,1106,0,303,1202,1,1,222,20102,1,221,3,21002,221,1,2,21101,259,0,1,21102,80,1,0,1106,0,225,21101,0,51,2,21101,0,91,0,1106,0,303,1202,1,1,223,20101,0,222,4,21101,259,0,3,21102,225,1,2,21101,225,0,1,21101,118,0,0,1105,1,225,20102,1,222,3,21102,1,152,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1105,1,259,1202,1,1,223,20101,0,221,4,21002,222,1,3,21102,1,17,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,108,20207,1,223,2,21002,23,1,1,21102,1,-1,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,22101,0,-3,1,21202,-2,1,2,22102,1,-1,3,21101,250,0,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21102,1,343,0,1105,1,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21202,-4,1,1,21102,1,384,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2105,1,0]
    affected = {}
    height = 2000
    width = 2000
    for y in range(height):
        for x in range(width):
            computer = IntCodeComputer(puzzleInput)
            computer.inputInstruction.append(x)
            computer.inputInstruction.append(y)
            while len(computer.output) == 0:
                computer.computeParameterModes(computer.program[computer.position])
                computer.position = computer.computeOperation(computer.position, computer.currentInstruction)
            affected[(x,y)] = computer.output[0]
    found = False
    for y in range(height):
        for x in range(width):
            if x + 100 < width and y + 100 < height:
                if affected[(x,y)] + affected[(x+99,y)] + affected[(x,y+99)] + affected[(x+99,y+99)] == 4:
                    print((x * 10000) + y)
                    found = True
                    break
        if found == True:
            break

if __name__ == '__main__':
    part1()
    part2()