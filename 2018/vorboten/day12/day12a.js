
const aoc = require('../lib/aoc.js');
const growth = inputfile('./day12t.txt', true);

const initial = '#..#.#..##......###...###';

let first = ('...' + initial + '...........').split('')

plantsum = plantline => {
  return plantline
    .map((char, index) => (char == '#'?index - 3:0))
    .reduce((summer, eq) => summer + eq)
}
     
growplants = (growcycle, current) => {
 for(i=0;i<current.length;i++) {
   
 }
 return current;
}

last = () => {
   return growplants(growth, first)
}

console.log(last());