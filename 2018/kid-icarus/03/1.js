const {readInput} = require('utils')

const solve = async () => {
  const input = await readInput(__dirname)
  const squares = input.map(x => x.split('@').pop().split(':').map(x => x.trim()))
  const box = []
  for (let i = 0; i < 1000; i++) {
    box[i] = new Array(1000).fill('-')
  }
  squares.forEach((square, index) => {
    const [x, y] = square[0].split(',').map(x => parseInt(x))
    const [width, height] = square[1].split('x').map(x => parseInt(x))
    for (let i = y; i < (y + height); i++) {
      for (let j = x; j < (x + width); j++) {
        if (box[i][j] !== '-') {
          box[i][j] = 'x'
        } else {
          box[i][j] = index
        }
      }
    }
  })

  return box.reduce((acc, row) => {
    const count = row.filter(col => col === 'x').length
    return acc + count
  },0)
}

solve().then(console.log)

module.exports = solve
