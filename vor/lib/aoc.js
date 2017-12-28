// aoc.js
module.exports = {
	inputfile: inputfile => {
		fs = require('fs')
		return fs.readFileSync(inputfile, 'utf8');
	}
};
