const aoc = require('../lib/aoc.js');
const changelist = inputfile('./day01.txt');
const result =  changelist
  .split('\n')
  .map(change => parseInt(change))
  .reduce((frequency, change) => frequency + change);
console.log(result);