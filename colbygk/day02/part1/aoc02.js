
const raw = require('./input.json');
const p = console.log;

const cksum = function (input) {
    var least = 0;
    var most = 0;
    var cksum = 0;
    input.forEach( (row) => {
        least = row[0];
        most = row[0];
        row.map( x => { if (x < least) { least = x; }; if (x > most) { most = x; }; return x; });
        cksum += (most - least);
    });
    return cksum;
};

raw.tests.forEach( (test) => {
    var sum = cksum(test.input);
    p(`Test expecting: ${test.answer} got: ${sum}: ${test.answer === sum ? "PASSED" : "FAILED"}`);
});


p(`Answer: ${cksum(raw.input)}`);
