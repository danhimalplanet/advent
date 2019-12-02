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

let restore = (compute, a, b) => {
    compute[1] = a;
    compute[2] = b;
    return compute
}

for(a = 0; a< 100; a++){
    for(b = 0; b < 100; b++) {
        resolve = instructions(restore(intcode(computer),a,b));
        if( resolve[0] == 19690720) {
            console.log(100 * a + b)
            a = 100; b = 100;
        }
    }
}
