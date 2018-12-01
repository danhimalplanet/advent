const aoc = require('../lib/aoc.js');
const changelist = inputfile('./day01.txt',true);

let freqlist = new Set(),
    found = false,
    frequency = 0;

while(!found) {
  changelist
    .some(change => {
      frequency += parseInt(change);  
      found = freqlist.has(frequency);
      freqlist.add(frequency);
      return found;
    });
}
console.log(frequency);
