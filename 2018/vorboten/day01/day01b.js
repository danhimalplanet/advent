const aoc = require('../lib/aoc.js');
const changelist = inputfile('./day01.txt');
let freqlist = [];
let newfreq, nextfreq = 0;
var found = false;
while(!found) {
nextfreq =  changelist
  .split('\n')
  .map(change => parseInt(change))
  .reduce((frequency, change) => {
    newfreq = frequency + change;  
    if(freqlist.includes(newfreq)) { 
      console.log(newfreq);
      freqlist = [];
      found = true;
    }
    freqlist.push(newfreq);
    return newfreq;
  },nextfreq);
}