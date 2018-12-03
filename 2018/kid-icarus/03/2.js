const {readInput} = require('utils')

const solve = async () => {
  const input = await readInput(__dirname)
  const squares = input.map(x => x.split('@').pop().split(':').map(x => x.trim())).map(
    (square, i) => {
      const index = i + 1
      const [x, y] = square[0].split(',').map(x => parseInt(x))
      const [width, height] = square[1].split('x').map(x => parseInt(x))
      return {
        x,y,width,height,index
      }
    }
  )

  const box = []
  for (let i = 0; i < 1000; i++) {
    box[i] = new Array(1000).fill('-')
  }

  squares.forEach(({x, y, width, height, index}) => {
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

  return squares.map(({x, y, width, height, index}) => {
    for (let i = y; i < (y + height); i++) {
      for (let j = x; j < (x + width); j++) {
        if (box[i][j] !== index) return false
      }
    }
    return index
  }).filter(x => x)
}

module.exports = solve
