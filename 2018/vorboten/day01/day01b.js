const aoc = require('../lib/aoc.js');
const changelist = inputfile('./day01.txt',true);

let freqlist = [],
    found = false,
    frequency = 0;

while(!found) {
  changelist
    .map(change => parseInt(change))
    .some(change => {
      frequency += change;  
      found = freqlist.includes(frequency);
      freqlist.push(frequency);
      return found;
    });
}
console.log(frequency);
