const {readFile} = require('fs')
const {promisify} = require('util')
const read = promisify(readFile)
const {join}= require('path')

async function getFrequency () {
  return read(join(__dirname, '1.txt'), {encoding: 'utf8'})
}

const getAnswer = async () => {
  const data = await getFrequency();
  const frequencies = new Set();
  let accumulator = 0;
  while(true) {
    for (let el of data.split('\n')) {
      const num = parseInt(el)
      if (isNaN(num)) continue;
      accumulator += num;
      if (frequencies.has(accumulator)) return accumulator
      frequencies.add(accumulator)
    }
  }
}

(async () => {
  console.log(await getAnswer());
})()
