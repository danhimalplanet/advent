let aoc = require('../lib/aoc.js')
let spread = aoc.inputfile('./day02.txt').split('\n')

let checksum = 0
spread.forEach(function(line){
	console.log('start ========')
	let elements = line.split(' ').map( Number )
	let tmin = Math.min.apply(null,elements);
	console.log(tmin)
	elements.map(function (a, b) {
		  	console.log(a, b)
		if (a % b == 0) {
		  	console.log('even', a, b)
//		  	checksum += a / b
		}
	});
});
// console.log(checksum)