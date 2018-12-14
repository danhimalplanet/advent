const aoc = require('../lib/aoc.js');
let polymer =  'dabAcCaCBAcCcaDA'; //inputfile('./day05.txt');

for(h = 10; h <= 34; h++){
  reg1 = new RegExp((h).toString(36) + (h).toString(36).toUpperCase(), 'g');
  reg2 = new RegExp((h).toString(36).toUpperCase() + (h).toString(36), 'g');
  while(!reg1.test(polymer) && !reg2.test(polymer)) {
    for(i = 10; i <= 34; i++){
      reg3 = new RegExp((i).toString(36) + (i).toString(36).toUpperCase(), 'g');
      reg4 = new RegExp((i).toString(36).toUpperCase() + (i).toString(36), 'g');
      while(!reg3.test(polymer) && !reg4.test(polymer)) {
        polymer = polymer
          .replace(reg3,'')
          .replace(reg4,'')
      }
    }
    }
console.log(h)
}
console.log(polymer)