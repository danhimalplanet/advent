const aoc = require('../lib/aoc.js');
const masslist = inputfile('./day01.txt');

calcfuel = (mass => Math.floor(parseInt(mass)/3) - 2);

let accum = 0;
totalfuel = masslist
    .map(mass => calcfuel(mass))
    .reduce((accum, fuel) => {
        return accum + fuel
    })

console.log(totalfuel)