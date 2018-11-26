const {day2, day2part2} = require('./day2')
const assert = require('assert')

const input1 = `5\t1\t9\t5
7\t5\t3
2\t4\t6\t8`

const input2 = `5\t9\t2\t8
9\t4\t7\t3
3\t8\t6\t5`

describe('Day 2', () => {
  it('Part 1: should calculate a checksum', () => {
    assert.equal(day2(input1), 18)
  })

  it('Part 2: should calculate evenly divisible checksum', () => {
    assert.equal(day2part2(input2), 9)
  })
})
