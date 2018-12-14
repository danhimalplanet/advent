const aoc = require('../lib/aoc.js');
const timestamps = inputfile('./day04test.txt', true);
let guardid,
    asleep, 
    awake,
    worstguard,
    worsttime = 0;
var guards = [];

stamps = timestamps
  .map(a => Date.parse(a.substring(1,17)) + ' ' + a.substring(12,14) + ' ' + a.substring(15,17) + a.substring(18,a.length))
  .sort((a,b) => parseInt(a.substring(0,15)) - parseInt(b.substring(0,15)))
  .forEach(a => {
    awake = 0;
    switch(a.substring(22,27)) {
      case 'Guard': // Guard on duty
        asleep = 0;

        dataPattern = /00\s[\d]+\s[\d]+[\s\w]+[\#]?([\d]*)/g;
        [match, guardid] = dataPattern.exec(a) || [];
        console.log('------------');
        console.log(typeof guardid);
        console.log('guard: ' + guardid);
    
        if (guards.indexOf(guardid) == -1) {
          guards[guardid] = [];
          guards[guardid].sleeptime = 0;
        }
        break;
      
      case 'falls': // Guard falls asleep
        dataPattern = /00\s([\d]+)\s([\d]+)[\s\w]/g;
        [match, hour, minute] = dataPattern.exec(a) || [];
        asleep = parseInt(minute);
        break;

      case 'wakes': // Guard wakes up
        dataPattern = /00\s([\d]+)\s([\d]+)[\s\w]/g;
        [match, hour, minute] = dataPattern.exec(a) || [];
        awake = parseInt(minute);

        guards[guardid].sleeptime = ((awake - asleep) + guards[guardid].sleeptime);

        if(worstguard) {
        //  console.log('worstguard: ' + worstguard, guards[worstguard].sleeptime)
          worstguard = (guards[guardid].sleeptime > guards[worstguard].sleeptime)? guardid: worstguard;
        } else {
          worstguard = guardid;
        //  console.log('worstguard:: ' + worstguard, guards[worstguard].sleeptime)
        }
        // console.log('asleep: ' + asleep )
        // console.log('awake: ' + awake )
        // console.log('sleeptime ' + guards[guardid].sleeptime)
        // console.log('diff ' + (awake - asleep))
        // console.log('total: ' + guards[guardid].sleeptime)
        for (i = asleep; i <= awake; i++) {
          //console.log(guardid, guards[guardid])
          if (typeof guards[guardid][i] == "undefined") {
            guards[guardid][i] = 0;
          }
          console.log('g: ' + guardid, i, guards[guardid][i])
          guards[guardid][i] += 1;
//          console.log(i, guards[guardid][i])
          if(worsttime) {
         //   console.log('worsttime: ' + worsttime)
            worsttime = (guards[guardid][i] > guards[worstguard][worsttime])? i: worsttime;
          } else {
            worsttime = i;
          //  console.log('worsttime:: ' + worsttime)
          }
        }
        break;
    }
  })  
 //console.log(worstguard , worsttime)
//console.log(guards)
console.log(guards[10][24])