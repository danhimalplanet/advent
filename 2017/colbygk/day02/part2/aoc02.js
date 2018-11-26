
const raw = require('./input.json');
const p = console.log;

const cksum = function (input) {
    var op1;
    var op2;
    var cksum = 0;
    input.forEach( (row) => {
        row.some( (x,i,a) => {
            return a.some( (y,j) => {
                if ( i !== j && x%y === 0 ) {
                     op1 = x;
                     op2 = y;
                     return true;
                 } else {
                     return false;
                 };
            });
        });
        cksum += (op1/op2);
    });
    return cksum;
};

raw.tests.forEach( (test) => {
    var sum = cksum(test.input);
    p(`Test expecting: ${test.answer} got: ${sum}: ${test.answer === sum ? "PASSED" : "FAILED"}`);
});


p(`Answer: ${cksum(raw.input)}`);
