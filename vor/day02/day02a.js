(() => {
  let aoc = require('../lib/aoc.js');
  let spread = aoc.inputfile('./day02.txt', true);

  let checksum = 0;
  spread.forEach(function(line){
  	let elements = line.split(' ').map( Number );
  	let tmin = Math.min.apply(null, elements);
  	let tmax = Math.max.apply(null, elements);
  	checksum += tmax - tmin;
  });
  console.log(checksum);
})()