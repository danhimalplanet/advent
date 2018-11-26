const {inverseCaptcha, inverseCaptcha2} = require('./day1')
const assert = require('assert')

describe('Day 1: Inverse captcha', () => {
  it('should add matching digits', () => {
    assert.equal(inverseCaptcha('1122'), 3)
    assert.equal(inverseCaptcha('1111'), 4)
    assert.equal(inverseCaptcha('1234'), 0)
    assert.equal(inverseCaptcha('91212129'), 9)
  })
})

describe('Day 1: Inverse captcha 2', () => {
  it('should add matching digits half the length of the array', () => {
    assert.equal(inverseCaptcha2('1212'), 6)
    assert.equal(inverseCaptcha2('1221'), 0)
    assert.equal(inverseCaptcha2('123425'), 4)
    assert.equal(inverseCaptcha2('123123'), 12)
    assert.equal(inverseCaptcha2('12131415'), 4)
  })
})
