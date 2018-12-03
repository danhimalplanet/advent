const aoc = require('../lib/aoc.js');
const swatches = inputfile('./day03.txt', true);

let squares = new Set(),
    dupes = new Set();

swatches.forEach((k) => { 
  let dataPattern = /^#([\d]+) @ ([\d]+),([\d]+): ([\d]+)x([\d]+)/g;
  let [match, index, left, top, width, height] = dataPattern.exec(k) || [];

  for(i = left; i < parseInt(left) + parseInt(width); i++) {
    for(j = top; j < parseInt(top) + parseInt(height); j++) {
      let plot = i + ':' + j;
      if(squares.has(plot)) {
        if(!dupes.has(plot)) {
          dupes.add(plot)
        }  
      } else {
      squares.add(plot)
      }
    }  
  }
})
console.log(dupes.size)
