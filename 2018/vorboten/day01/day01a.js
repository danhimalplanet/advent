const aoc = require('../lib/aoc.js');
const changelist = inputfile('./day01.txt', true);
const result =  changelist
  .map(change => parseInt(change))
  .reduce((frequency, change) => frequency + parseInt(change));
console.log(result);