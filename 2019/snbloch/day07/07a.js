var Combinatorics = require('js-combinatorics');

var puzzleInput = [3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99];
var diagnostic = [];
var inputInstruction = [];
var output = [];
var currentInstruction;
var firstParameterMode;
var secondParameterMode;
var thirdParameterMode;

function computeParameterModes (instruction) {
    switch (instruction.toString().length) {
        case 1:
            currentInstruction = parseInt(instruction.toString().slice(0));
            firstParameterMode = 0;
            secondParameterMode = 0;
            thirdParameterMode = 0;
            break;
        case 2:
            currentInstruction = parseInt(instruction.toString().slice(0));
            firstParameterMode = 0;
            secondParameterMode = 0;
            thirdParameterMode = 0;
            break;
        case 3:
            currentInstruction = parseInt(instruction.toString().slice(1));
            firstParameterMode = parseInt(instruction.toString()[0]);
            secondParameterMode = 0;
            thirdParameterMode = 0;
            break;
        case 4:
            currentInstruction = parseInt(instruction.toString().slice(2));
            firstParameterMode = parseInt(instruction.toString()[1]);
            secondParameterMode = parseInt(instruction.toString()[0]);
            thirdParameterMode = 0;
            break;
        case 5:
            currentInstruction = parseInt(instruction.toString().slice(3));
            firstParameterMode = parseInt(instruction.toString()[2]);
            secondParameterMode = parseInt(instruction.toString()[1]);
            thirdParameterMode = parseInt(instruction.toString()[0]);
            break;
    }
}

function computeOperation (position, instruction) {
    var firstParameter;
    var secondParameter;
    switch (firstParameterMode) {
        case 0:
            firstParameter = parseInt(diagnostic[diagnostic[position + 1]]);
            break;
        case 1:
            firstParameter = parseInt([diagnostic[position + 1]]);
            break;
    }
    switch (secondParameterMode) {
        case 0:
            secondParameter = parseInt(diagnostic[diagnostic[position + 2]]);
            break;
        case 1:
            secondParameter = parseInt([diagnostic[position + 2]]);
            break;
    }

    switch(instruction) {
        case 99:
            return -1;
        case 1:
            diagnostic[diagnostic[position + 3]] = firstParameter + secondParameter;
            return (position + 4);
        case 2:
            diagnostic[diagnostic[position + 3]] = firstParameter * secondParameter;
            return (position + 4);
        case 3:
            diagnostic[diagnostic[position + 1]] = inputInstruction.shift();
            return (position + 2);
        case 4:
            output.push(firstParameter);
            return (position + 2);
        case 5:
            if (firstParameter != 0) {
                return secondParameter;
            } 
            else {
                return (position + 3);
            }
            break;
        case 6:
            if (firstParameter == 0) {
                return secondParameter;
            }
            else {
                return (position + 3);
            }
            break;
        case 7:
            if (firstParameter < secondParameter) {
                diagnostic[diagnostic[position + 3]] = 1;
                return (position + 4);
            }
            else {
                diagnostic[diagnostic[position + 3]] = 0;
                return (position + 4);
            }
            break;
        case 8:
            if (firstParameter == secondParameter) {
                diagnostic[diagnostic[position + 3]] = 1;
                return (position + 4);
            }
            else {
                diagnostic[diagnostic[position + 3]] = 0;
                return (position + 4);
            }
            break;
    }
}

function main() {
    var maxThrusterOutput = 0;
    var sequences = Combinatorics.permutation([0,1,2,3,4]).toArray();
    sequences.forEach(function (i) {
        var amplifierOutput = 0;
        diagnostic = puzzleInput.slice(0);
        i.forEach(function (e) {
            inputInstruction.push(e);
            inputInstruction.push(amplifierOutput);
            var position = 0;
            while (position != -1) {
                computeParameterModes(diagnostic[position]);
                position = computeOperation(position, currentInstruction);
            }
            amplifierOutput = output.pop();
        });
        if (amplifierOutput > maxThrusterOutput) { 
            maxThrusterOutput = amplifierOutput;
        }
    });
    console.log(maxThrusterOutput);
}

main();