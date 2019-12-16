var Combinatorics = require('js-combinatorics');

var puzzleInput = [3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99];

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
            case 5:
                if (firstParameter != 0) {
                    return secondParameter;
                } 
                else {
                    return (this.position + 3);
                }
                break;
            case 6:
                if (firstParameter == 0) {
                    return secondParameter;
                }
                else {
                    return (this.position + 3);
                }
                break;
            case 7:
                if (firstParameter < secondParameter) {
                    this.program[this.program[this.position + 3]] = 1;
                    return (this.position + 4);
                }
                else {
                    this.program[this.program[this.position + 3]] = 0;
                    return (this.position + 4);
                }
                break;
            case 8:
                if (firstParameter == secondParameter) {
                    this.program[this.program[this.position + 3]] = 1;
                    return (this.position + 4);
                }
                else {
                    this.program[this.program[this.position + 3]] = 0;
                    return (this.position + 4);
                }
                break; 
        }
    }
}

function main() {
    var maxThrusterOutput = 0;
    var sequences = Combinatorics.permutation([0,1,2,3,4]).toArray();
    sequences.forEach(function (i) {
        var amplifierOutput = 0;
        i.forEach(function (e) {
            computer = new IntCodeComputer(puzzleInput);
            computer.inputInstruction.push(e);
            computer.inputInstruction.push(amplifierOutput);
            while (computer.position != -1) {
                computer.computeParameterModes(computer.program[computer.position]);
                computer.position = computer.computeOperation(computer.position, computer.currentInstruction);
            }
            amplifierOutput = computer.output.pop();
        });
        if (amplifierOutput > maxThrusterOutput) { 
            maxThrusterOutput = amplifierOutput;
        }
    });
    console.log(maxThrusterOutput);
}

main();