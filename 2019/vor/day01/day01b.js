const aoc = require('../lib/aoc.js');
const masslist = inputfile('./day01.txt');

calcfuel = (mass => Math.floor(parseInt(mass)/3) - 2);

recursefuel = (mass => {
    fuelweight = 0;
    let fuel = calcfuel(mass);
    while (fuel > 0) {
        fuelweight += fuel
        fuel = calcfuel(fuel)
    }
    return fuelweight
})

let accum = 0;
totalfuel = masslist
    .map(mass => recursefuel(mass))
    .reduce((accum, fuel) => {
        return accum + fuel
    })

console.log(totalfuel)
