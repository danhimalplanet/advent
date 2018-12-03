const assert = require('assert')
const oneA = require('./1')

it('works', () => {
  oneA().then(answer => assert.equal(answer, 4))
})