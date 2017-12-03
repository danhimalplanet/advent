const maxMinusMin = row => row.reduce((acc, curr, i, arr) => {
  let num = parseInt(curr)
  if (num > acc[0]) acc[0] = curr
  if (num < acc[1]) acc[1] = curr
  if (i === arr.length - 1) return acc[0] - acc[1]
  return acc
}, [-Infinity, Infinity])

const sum = (a, b) => a + b

const parse = input => input.split('\n')
  .map(row => row.split('\t'))

const day2 = input => parse(input)
  .map(maxMinusMin)
  .reduce(sum)

const evenlyDivisibleQuotient = (acc, curr, i, arr) => {
  if (acc) return acc

  for (let j = 0; j < arr.length; j++) {
    if (i === j) continue;
    if (curr % arr[j] === 0) return curr / arr[j]
    if (arr[j] % curr === 0) return arr[j] / curr
  }
}

const day2part2 = input => parse(input)
  .map(row => row.reduce(evenlyDivisibleQuotient, undefined))
  .reduce(sum)

module.exports = {
  day2,
  day2part2
}
