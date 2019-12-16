var puzzleInput = [3,225,1,225,6,6,1100,1,238,225,104,0,1001,191,50,224,101,-64,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,2,150,218,224,1001,224,-1537,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1002,154,5,224,101,-35,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1102,76,17,225,1102,21,44,224,1001,224,-924,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,101,37,161,224,101,-70,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,102,46,157,224,1001,224,-1978,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1102,5,29,225,1101,10,7,225,1101,43,38,225,1102,33,46,225,1,80,188,224,1001,224,-73,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1101,52,56,225,1101,14,22,225,1101,66,49,224,1001,224,-115,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1101,25,53,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,226,224,1002,223,2,223,1005,224,329,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,344,1001,223,1,223,8,677,677,224,102,2,223,223,1006,224,359,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,374,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,419,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,434,101,1,223,223,1008,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,226,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,108,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,539,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,599,1001,223,1,223,1107,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,629,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226];

class IntCodeComputer {
    constructor(program) {
        this.program = program;
        this.inputInstruction = [];
        this.output = [];
        this.firstParameterMode;
        this.secondParameterMode;
        this.thirdParameterMode;
        this.position = 0;
        this.currentInstruction;
    }
    
    computeParameterModes (instruction) {
        switch (instruction.toString().length) {
            case 1:
                this.currentInstruction = parseInt(instruction.toString().slice(0));
                this.firstParameterMode = 0;
                this.secondParameterMode = 0;
                this.thirdParameterMode = 0;
                break;
            case 2:
                this.currentInstruction = parseInt(instruction.toString().slice(0));
                this.firstParameterMode = 0;
                this.secondParameterMode = 0;
                this.thirdParameterMode = 0;
                break;
            case 3:
                this.currentInstruction = parseInt(instruction.toString().slice(1));
                this.firstParameterMode = parseInt(instruction.toString()[0]);
                this.secondParameterMode = 0;
                this.thirdParameterMode = 0;
                break;
            case 4:
                this.currentInstruction = parseInt(instruction.toString().slice(2));
                this.firstParameterMode = parseInt(instruction.toString()[1]);
                this.secondParameterMode = parseInt(instruction.toString()[0]);
                this.thirdParameterMode = 0;
                break;
            case 5:
                this.currentInstruction = parseInt(instruction.toString().slice(3));
                this.firstParameterMode = parseInt(instruction.toString()[2]);
                this.secondParameterMode = parseInt(instruction.toString()[1]);
                this.thirdParameterMode = parseInt(instruction.toString()[0]);
                break;
        }
    }
    
    computeOperation (position, instruction) {
        var firstParameter;
        var secondParameter;
        switch (this.firstParameterMode) {
            case 0:
                firstParameter = parseInt(this.program[this.program[this.position + 1]]);
                break;
            case 1:
                firstParameter = parseInt(this.program[this.position + 1]);
                break;
        }
        switch (this.secondParameterMode) {
            case 0:
                secondParameter = parseInt(this.program[this.program[this.position + 2]]);
                break;
            case 1:
                secondParameter = parseInt(this.program[this.position + 2]);
                break;
        }
    
        switch(instruction) {
            case 99:
                return -1;
            case 1:
                this.program[this.program[this.position + 3]] = firstParameter + secondParameter;
                return (this.position + 4);
            case 2:
                this.program[this.program[this.position + 3]] = firstParameter * secondParameter;
                return (this.position + 4);
            case 3:
                this.program[this.program[this.position + 1]] = this.inputInstruction.shift();
                return (position + 2);
            case 4:
                this.output.push(firstParameter);
                return (this.position + 2); 
        }
    }
}

function main() {
    computer = new IntCodeComputer(puzzleInput);
    computer.inputInstruction.push(1);
    while (computer.position != -1) {
        computer.computeParameterModes(computer.program[computer.position]);
        computer.position = computer.computeOperation(computer.position, computer.currentInstruction);
    }
console.log(computer.output);
}

main();