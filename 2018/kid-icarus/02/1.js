const {readInput} = require('utils')

const solve = async () => {
  const input = await readInput(__dirname, {pop: false})
  const totals = input.reduce((acc, word) => {
    const letters = {}
    let hasDub, hasTrip

    for (let letter of word) {
      if (letters[letter]) {
        letters[letter]++
      } else {
        letters[letter] = 1
      }
    }

    Object.entries(letters).forEach(([k, v]) => {
      if (v === 2) hasDub = true
      if (v === 3) hasTrip = true
    })

    if (hasDub) acc.dubs++
    if (hasTrip) acc.trips++
    return acc
  }, {dubs: 0, trips: 0})

  return totals.dubs * totals.trips
}

solve().then(console.log)
