const {readFile} = require('fs')
const {promisify} = require('util')
const read = promisify(readFile)

async function getFrequency () {
  return read('./1.txt', {encoding: 'utf8'})
}

(async () => {
  const data = await getFrequency();
  const answer = data.split('\n').reduce((a, b) => {
    const num = parseInt(b)
    if (isNaN(num)) return a
    return a + num
  }, 0)
  console.log(answer)
})()

