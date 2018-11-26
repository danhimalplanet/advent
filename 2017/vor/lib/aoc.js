// aoc.js
module.exports = {
	inputfile: (inputfile, newline = false) => {
		fs = require('fs')
    output = fs.readFileSync(inputfile, 'utf8')
		return (newline)? output.split('\n') : output
	},
  allcompare: (inputArray, callback) => {
    inputArray.forEach(function(wordA, indexA){
      inputArray.forEach(function(wordB, indexB){
        callback(wordA, wordB, indexA, indexB)
      })
    })
  },
}
