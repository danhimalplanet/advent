const {readFile} = require('fs')
const {promisify} = require('util')
const read = promisify(readFile)
const {join}= require('path')

async function getFrequency () {
  return read(join(__dirname, '1.txt'), {encoding: 'utf8'})
}

const getAnswer = async () => {
  const data = await getFrequency();
  const frequencyTable = {
    0: true
  }
  let accumulator = 0;
  while(true) {
    for (let e of data.split('\n')) {
      const num = parseInt(e)
      if (isNaN(num)) continue;
      accumulator += num
      if (frequencyTable[accumulator]) return accumulator
      frequencyTable[accumulator] = true
    }
  }
}

(async () => {
  console.log(await getAnswer());
})()
