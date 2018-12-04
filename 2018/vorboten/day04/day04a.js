const aoc = require('../lib/aoc.js');
const timestamps = inputfile('./day04.txt', true);
let guardId, 
    match, 
    asleep, 
    awake, 
    guards = [];

stamps = timestamps
  .map(a => Date.parse(a.substring(1,17)) + a.substring(18,a.length))
  .sort((a,b) => parseInt(a.substring(0,15)) - parseInt(b.substring(0,15)))
  .forEach(a => {
    switch(a.substring(16,21)) {
      case 'Guard': // Guard on duty
        dataPattern = /\#([\d]+)/g;
        [match, guardId] = dataPattern.exec(a) || [];
        asleep = 0;
        awake = 0;
        break;
      case 'falls': // Guard falls asleep
        asleep = a.substring(0,15)
        awake = 0;
        break;
      case 'wakes': // Guard wakes up
        awake = a.substring(0,15)
        if(guardId in guards) {
          let sleepytime = (parseInt(awake) - parseInt(asleep))/ (1000 * 60)
          guards[guardId] = guards[guardId] + sleepytime;
        } else {
          let sleepytime = (parseInt(awake) - parseInt(asleep))/ (1000 * 60)
          guards[guardId] = sleepytime;
        }
        asleep = 0;
        break;
    }
  })  
//  console.log(guards[393])
console.log(guards)
// let dataPattern = /\[([\d]+)-([\d]+)-([\d]+) ([\d]+):([\d]+)\]([\s\w\d\#]+)/g;
// let [match, year, month, day, hour, minute, copy] = dataPattern.exec(a) || [];