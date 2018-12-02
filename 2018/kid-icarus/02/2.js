const {readInput} = require('utils')

const solve = async () => {
  const input = await readInput(__dirname, {pop: false})
  // loop through each word
  for (let i = 0; i < input.length; i++) {
    let word = input[i]
    // compare it to every other word
    for (let j = 0; j < input.length; j++) {
      if (j === i) continue
      let otherWord = input[j]
      let mismatchCount = 0 //reset count for every word
      let commonLetters = ''
      // compare letters of both words
      for (let k = 0; k < word.length; k++) {
        if (word[k] === otherWord[k]) {
          commonLetters += word[k]
        } else {
          mismatchCount++
        }
      }

      if (mismatchCount === 1) {
        return commonLetters
      } else {
        continue
      }
    }
  }
}

solve().then(console.log)
