var totalFuel = 0

function fuelFromMass(mass){
    mass /= 3;
    mass = Math.floor(mass);
    mass -= 2;
    return mass;
}

require('fs').readFileSync('input.txt', 'utf-8').split(/\r?\n/).forEach(function(line){
    totalFuel += fuelFromMass(parseInt(line));
  })

console.log(totalFuel)