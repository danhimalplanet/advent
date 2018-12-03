const aoc = require('../lib/aoc.js');
const swatches = inputfile('./day03.txt', true);

let squares = new Set(),
    dupes = new Set();
    lappers = new Set();

swatches.forEach((k) => { 
  let dataPattern = /^#([\d]+) @ ([\d]+),([\d]+): ([\d]+)x([\d]+)/g;
  let [match, index, left, top, width, height] = dataPattern.exec(k) || [];
  potential = true;
  for(i = left; i < parseInt(left) + parseInt(width); i++) {
    for(j = top; j < parseInt(top) + parseInt(height); j++) {
      let plot = i + ':' + j;
      if(squares.has(plot)) {
        if(!dupes.has(plot)) {
          dupes.add(plot)
          if(!lappers.has(index)){
            lappers.add(index);
          }
        }  
      } else {
      squares.add(plot)
      }
    }  
  }
})

swatches.forEach((k) => { 
  let dataPattern = /^#([\d]+) @ ([\d]+),([\d]+): ([\d]+)x([\d]+)/g;
  let [match, index, left, top, width, height] = dataPattern.exec(k) || [];

  if(!lappers.has(index)) {
    let potential = true;
    for(i = left; i < parseInt(left) + parseInt(width); i++) {
      for(j = top; j < parseInt(top) + parseInt(height); j++) {
        let plot = i + ':' + j;
        if(dupes.has(plot)) {
            i = parseInt(left) + parseInt(width);
            j = parseInt(top) + parseInt(height);
            potential = false;
        }  
      }  
    }
    if(potential) {
      console.log(index);
      return;
    }
  }
})

