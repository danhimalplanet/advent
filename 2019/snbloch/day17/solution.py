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
    puzzleInput = [1,330,331,332,109,3546,1101,0,1182,15,1101,1481,0,24,1001,0,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1105,1,18,1008,571,0,571,1001,15,1,15,1008,15,1481,570,1006,570,14,21102,58,1,0,1106,0,786,1006,332,62,99,21101,0,333,1,21101,0,73,0,1106,0,579,1101,0,0,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,1002,574,1,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21102,1,340,1,1106,0,177,21102,1,477,1,1106,0,177,21101,0,514,1,21102,1,176,0,1105,1,579,99,21102,1,184,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,102,1,572,1182,21102,375,1,1,21101,211,0,0,1106,0,579,21101,1182,11,1,21101,0,222,0,1106,0,979,21102,388,1,1,21102,1,233,0,1106,0,579,21101,1182,22,1,21102,1,244,0,1106,0,979,21101,0,401,1,21102,255,1,0,1106,0,579,21101,1182,33,1,21102,266,1,0,1105,1,979,21102,414,1,1,21102,1,277,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21102,1,1182,1,21102,1,313,0,1105,1,622,1005,575,327,1102,1,1,575,21101,0,327,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,12,18,0,109,4,2102,1,-3,587,20101,0,0,-1,22101,1,-3,-3,21101,0,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1106,0,597,109,-4,2106,0,0,109,5,2102,1,-4,630,20102,1,0,-2,22101,1,-4,-4,21101,0,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20102,1,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21101,0,702,0,1105,1,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,731,1,0,1105,1,786,1106,0,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21102,1,756,0,1105,1,786,1105,1,774,21202,-1,-11,1,22101,1182,1,1,21101,0,774,0,1106,0,622,21201,-3,1,-3,1106,0,640,109,-5,2106,0,0,109,7,1005,575,802,21001,576,0,-6,20102,1,577,-5,1106,0,814,21102,1,0,-1,21102,0,1,-5,21102,0,1,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,59,-3,22201,-6,-3,-3,22101,1481,-3,-3,2101,0,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1105,1,924,1205,-2,873,21102,35,1,-4,1105,1,924,2101,0,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,1202,-3,1,895,1101,0,2,0,2101,0,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,921,21002,0,1,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,59,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,35,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21102,973,1,0,1105,1,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21102,1,-4,-2,1106,0,1041,21101,0,-5,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,1202,-2,1,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1202,-2,1,0,1105,1,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1105,1,989,21101,0,439,1,1106,0,1150,21102,477,1,1,1106,0,1150,21101,0,514,1,21102,1,1149,0,1105,1,579,99,21101,0,1157,0,1106,0,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,1201,-4,0,0,109,-6,2105,1,0,6,13,27,13,6,1,11,1,27,1,11,1,6,1,11,1,27,1,11,1,6,1,11,1,27,1,11,1,6,1,11,1,27,1,11,1,6,1,11,1,27,1,11,1,6,1,11,1,1,9,9,11,9,1,6,1,11,1,1,1,7,1,9,1,7,1,1,1,9,1,6,1,11,13,7,1,7,1,1,1,9,1,6,1,13,1,7,1,1,1,7,1,7,1,1,1,9,1,6,1,13,1,7,1,1,1,5,11,1,1,9,1,6,1,13,1,7,1,1,1,5,1,1,1,9,1,9,1,6,11,3,1,7,1,1,1,5,1,1,1,9,1,1,9,16,1,3,1,7,1,1,1,5,1,1,1,9,1,1,1,24,1,3,1,7,13,7,1,1,1,24,1,3,1,9,1,5,1,1,1,1,1,7,1,1,1,24,1,3,1,9,9,1,1,7,11,16,1,3,1,15,1,3,1,9,1,7,1,12,9,15,1,3,1,9,1,7,1,16,1,19,1,3,1,9,1,7,1,16,1,19,11,3,1,7,1,16,1,23,1,5,1,3,1,7,1,8,9,23,11,7,1,8,1,37,1,11,1,8,1,37,1,11,1,8,1,37,1,11,1,8,1,37,1,11,1,8,1,37,1,11,1,8,1,37,13,8,1,58,1,58,1,58,1,58,1,50,9,50]
    grid = []
    computer = IntCodeComputer(puzzleInput)
    while computer.position is not None:
        computer.computeParameterModes(computer.program[computer.position])
        computer.position = computer.computeOperation(computer.position, computer.currentInstruction)
    row = ''
    for i in computer.output:
        if i == 35:
            row += '#'
        elif i == 46:
            row += '.'
        elif i == 94:
            row += '^'
        elif i == 116:
            row += 'v'
        elif i == 60:
            row += '<'
        elif i == 62:
            row += '>'
        elif i == 10 and len(row):
            grid.append(row)
            row = ''
    alignment_sum = 0
    for y in range(1, len(grid) - 2):
        for x in range(1, len(grid[y]) - 2):
            if grid[y][x] == '#' and grid[y - 1][x] == '#' and grid[y + 1][x] == '#' and grid[y][x - 1] == '#' and grid[y][x + 1] == '#':
                alignment_sum += y * x
    print(alignment_sum)

def part2():
    puzzleInput = [2,330,331,332,109,3546,1101,0,1182,15,1101,1481,0,24,1001,0,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1105,1,18,1008,571,0,571,1001,15,1,15,1008,15,1481,570,1006,570,14,21102,58,1,0,1106,0,786,1006,332,62,99,21101,0,333,1,21101,0,73,0,1106,0,579,1101,0,0,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,1002,574,1,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21102,1,340,1,1106,0,177,21102,1,477,1,1106,0,177,21101,0,514,1,21102,1,176,0,1105,1,579,99,21102,1,184,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,102,1,572,1182,21102,375,1,1,21101,211,0,0,1106,0,579,21101,1182,11,1,21101,0,222,0,1106,0,979,21102,388,1,1,21102,1,233,0,1106,0,579,21101,1182,22,1,21102,1,244,0,1106,0,979,21101,0,401,1,21102,255,1,0,1106,0,579,21101,1182,33,1,21102,266,1,0,1105,1,979,21102,414,1,1,21102,1,277,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21102,1,1182,1,21102,1,313,0,1105,1,622,1005,575,327,1102,1,1,575,21101,0,327,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,12,18,0,109,4,2102,1,-3,587,20101,0,0,-1,22101,1,-3,-3,21101,0,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1106,0,597,109,-4,2106,0,0,109,5,2102,1,-4,630,20102,1,0,-2,22101,1,-4,-4,21101,0,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20102,1,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21101,0,702,0,1105,1,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,731,1,0,1105,1,786,1106,0,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21102,1,756,0,1105,1,786,1105,1,774,21202,-1,-11,1,22101,1182,1,1,21101,0,774,0,1106,0,622,21201,-3,1,-3,1106,0,640,109,-5,2106,0,0,109,7,1005,575,802,21001,576,0,-6,20102,1,577,-5,1106,0,814,21102,1,0,-1,21102,0,1,-5,21102,0,1,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,59,-3,22201,-6,-3,-3,22101,1481,-3,-3,2101,0,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1105,1,924,1205,-2,873,21102,35,1,-4,1105,1,924,2101,0,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,1202,-3,1,895,1101,0,2,0,2101,0,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,921,21002,0,1,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,59,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,35,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21102,973,1,0,1105,1,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21102,1,-4,-2,1106,0,1041,21101,0,-5,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,1202,-2,1,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1202,-2,1,0,1105,1,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1105,1,989,21101,0,439,1,1106,0,1150,21102,477,1,1,1106,0,1150,21101,0,514,1,21102,1,1149,0,1105,1,579,99,21101,0,1157,0,1106,0,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,1201,-4,0,0,109,-6,2105,1,0,6,13,27,13,6,1,11,1,27,1,11,1,6,1,11,1,27,1,11,1,6,1,11,1,27,1,11,1,6,1,11,1,27,1,11,1,6,1,11,1,27,1,11,1,6,1,11,1,1,9,9,11,9,1,6,1,11,1,1,1,7,1,9,1,7,1,1,1,9,1,6,1,11,13,7,1,7,1,1,1,9,1,6,1,13,1,7,1,1,1,7,1,7,1,1,1,9,1,6,1,13,1,7,1,1,1,5,11,1,1,9,1,6,1,13,1,7,1,1,1,5,1,1,1,9,1,9,1,6,11,3,1,7,1,1,1,5,1,1,1,9,1,1,9,16,1,3,1,7,1,1,1,5,1,1,1,9,1,1,1,24,1,3,1,7,13,7,1,1,1,24,1,3,1,9,1,5,1,1,1,1,1,7,1,1,1,24,1,3,1,9,9,1,1,7,11,16,1,3,1,15,1,3,1,9,1,7,1,12,9,15,1,3,1,9,1,7,1,16,1,19,1,3,1,9,1,7,1,16,1,19,11,3,1,7,1,16,1,23,1,5,1,3,1,7,1,8,9,23,11,7,1,8,1,37,1,11,1,8,1,37,1,11,1,8,1,37,1,11,1,8,1,37,1,11,1,8,1,37,1,11,1,8,1,37,13,8,1,58,1,58,1,58,1,58,1,50,9,50]
    computer = IntCodeComputer(puzzleInput)
    movement_routine = 'A,A,B,C,B,C,B,A,C,A\n'
    function_a = 'R,8,L,12,R,8\n'
    function_b = 'L,10,L,10,R,8\n'
    function_c = 'L,12,L,12,L,10,R,10\n'
    video_feed_enabled = 'n\n'
    for i in movement_routine:
        computer.inputInstruction.append(ord(i))
    for i in function_a:
        computer.inputInstruction.append(ord(i))
    for i in function_b:
        computer.inputInstruction.append(ord(i))
    for i in function_c:
        computer.inputInstruction.append(ord(i))
    for i in video_feed_enabled:
        computer.inputInstruction.append(ord(i))
    while computer.position is not None:
        computer.computeParameterModes(computer.program[computer.position])
        computer.position = computer.computeOperation(computer.position, computer.currentInstruction)
    print(computer.output[-1])

if __name__ == '__main__':
    part1()
    part2()