const aoc = require('../lib/aoc.js');
const computer = inputfile('./day02.txt', false);

let intcode = compute => compute 
                        .split(",")
                        .map(node => Number(node))


let instructions = compute => {
    for(i=0; i < compute.length;i += 4) {
        opcode = compute[i]
        input1 = compute[i + 1]
        input2 = compute[i + 2]
        output = compute[i + 3]
        switch (opcode) {
            case 1:
                compute[output] = compute[input1] + compute[input2]
                break;
            case 2:
                compute[output] = compute[input1] * compute[input2]
                break;
            case 99:
                i = compute.length;   
                break;
        }
    }
    return compute;
}

let restore = compute => {
    compute[1] = 12;
    compute[2] = 2;
    return compute
}

resolve = instructions(restore(intcode(computer)))

console.log(resolve[0])
