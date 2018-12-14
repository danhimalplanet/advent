const aoc = require('../lib/aoc.js');
const instructions = inputfile('./day07test.txt', true);

var order = '',
    queue = [],
    prereqs = [],
    prevstep = '';

    cyclequeue = () => {
      if(queue.length != 0) {
        queue.sort()
        for(i = 0; i < queue.length; i++) {
          let target = queue[i];
          if(!prereqs.includes(target)) {
            if(!order.includes(target)) {
              order += target;
              prevstep = target;
              prereqs.forEach(a => { 
                console.log(a);
                if(a.has(target)) a.delete(target);
                return a;
              })
            };
            queue.shift();
            break;
          }
        }
      }
    }

    results = instructions.map(inst => [inst.substr(5,1), inst.substr(36,1)]);

    results.forEach(inst => { // Create Prereqs
        if(prereqs[inst[1]] == undefined) {
          console.log('Set: ' + inst[1], inst[0])
          
          prereqs.push(inst[1]);
          prereqs[inst[1]] = new Set();
        }
        prereqs[inst[1]].add(inst[0]);
        console.log('prereqs: ' + prereqs)
        return inst;
      });

      results.forEach(inst => {
      if(inst[0] != prevstep) {
          cyclequeue(queue);
          if(!order.includes(inst[0]) && !queue.includes(inst[0])) {
            queue.push(inst[0]);
            cyclequeue(queue);
          }
      }
      if(!order.includes(inst[1]) && !queue.includes(inst[1])) {
        queue.push(inst[1])
      };
    })



    console.log(order)

