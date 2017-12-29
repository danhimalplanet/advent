(function(){
  let aoc = require('../lib/aoc.js')
  let secret = aoc.inputfile('./day01.txt')

  let sumtotal = 0
  let comparer = 0
  let jump = 1

  for (let m = 0; m < secret.length; m++) {
    let start = parseInt(secret.charAt(m))
    
    if (m + jump >= secret.length) {
      comparer = parseInt(secret.charAt(jump + m - secret.length))
    } else {
      comparer = parseInt(secret.charAt(jump + m))
    }
    if (start == comparer) {sumtotal += start}
  }

  console.log(sumtotal)  
})()