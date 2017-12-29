(function(){
	let aoc = require('../lib/aoc.js')
	let spread = aoc.inputfile('./day02.txt').split('\n')

	let checksum = 0
	spread.forEach(function(line){
		let elements = line.split(' ').map( Number ).sort()
		elements.forEach(function(numA){
			elements.forEach(function(numB){
				if (numA != numB && numA > numB && numA % numB == 0) {
					checksum += (numA / numB)
				}
			})
		})
	});
	console.log(checksum)
})()