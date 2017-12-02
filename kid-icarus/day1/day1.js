const inverseCaptcha = input => input.split('').reduce((acc, curr, i, arr) => {
  if (i < arr.length - 1 && curr === arr[i + 1]) return acc + parseInt(curr)
  if (i === arr.length - 1 && curr === arr[0]) return acc + parseInt(curr)
  return acc
}, 0)

const inverseCaptcha2 = input => input.split('').reduce((acc, curr, i, arr) => {
  const step = arr.length / 2
  const index = i + step < arr.length ? i + step : i + step - arr.length

  if (curr === arr[index]) return acc + parseInt(curr)
  return acc
}, 0)

module.exports = {
  inverseCaptcha,
  inverseCaptcha2
}
