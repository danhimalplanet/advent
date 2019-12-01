var totalFuel = 0

function fuelFromMass(mass){
    mass /= 3;
    mass = Math.floor(mass);
    mass -= 2;
    return mass;
}

require('fs').readFileSync('input.txt', 'utf-8').split(/\r?\n/).forEach(function(line){
    var fuel = fuelFromMass(parseInt(line));
    fuelToAdd = fuelFromMass(parseInt(line));
    while (fuelToAdd > 0) {
      if (fuelFromMass(fuelToAdd) > 0){
        fuel += fuelFromMass(fuelToAdd);
        fuelToAdd = fuelFromMass(fuelToAdd);
      }
      else {
        break;
      }
    }
    totalFuel += fuel;
  });

console.log(totalFuel)