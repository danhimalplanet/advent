const aoc = require('../lib/aoc.js');
const boxes = inputfile('./day02.txt', true);

let twos = 0;
let threes = 0;
let boxlist = new Set();

const result =  boxes.forEach(box =>{
  let foundtwo = false;
  let foundthree = false;

  for (let char of String.prototype.concat(...new Set(box))) {
    regex = new RegExp(char, "g");
    if(box.match(regex)) {
      switch (box.match(regex).length) {
        case 2:
          if(!foundtwo) twos++
          foundtwo = true;
          break;
        case 3:
          if(!foundthree) threes++
          foundthree = true;
          break;
       }
    }
  }
})
console.log (`checksum = ${twos * threes}`)