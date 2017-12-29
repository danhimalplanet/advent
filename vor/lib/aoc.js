// aoc.js
module.exports = {
	inputfile: (inputfile) => {
		fs = require('fs')
		return fs.readFileSync(inputfile, 'utf8')
	},
  allcompare: (inputArray, callback) => {
    inputArray.forEach(function(wordA, indexA){
      inputArray.forEach(function(wordB, indexB){
        callback(wordA, wordB, indexA, indexB)
      }
    }
  },
}
