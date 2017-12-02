
const raw = require('./input.json');
const p = console.log;

const aoc01 = function(input) {
  var data = input.split('').map( x => parseInt(x) );
  var last = data[data.length - 1];
  var count = 0;
  var forward = data.length / 2;
  data.map((x,j) => { if (x === data[(j+forward)%data.length]) { count += x; }; return x;});
  return count;
};

raw.tests.forEach( (test) => {
  var answer = aoc01(test.input);
  p(`Test: ${test.input} expect ${test.answer}, got: ${answer}, ${answer === test.answer ? 'PASSED' : 'FAILED'}`);
});

p(`Final answer: ${aoc01(raw.input)}`);


