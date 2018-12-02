const aoc = require('../lib/aoc.js');
const boxes = inputfile('./day02.txt', true);

let boxlist = new Set();
const result =  boxes.forEach(box =>{
  for (let char of String.prototype.concat(...new Set(box))) {
    regex = new RegExp(char, "g");
    if(box.match(regex) && (box.match(regex).length === 2 ||  box.match(regex).length === 3)) boxlist.add(box);
  }
})

for (let box of boxlist) {
  for(let box2 of boxlist) {
    let diffcount = 0;
    let commonality = '';
    if (box2 != box) {
      for(i = 0;i < box.length; i++) {
        if(box.charAt(i) != box2.charAt(i) ) {
          if(diffcount < 2) { 
            diffcount++
          } else {
            break;
          }
        } else {
          commonality += box.charAt(i);
        }
      }
    }
    if(diffcount == 1) {
      console.log(`${commonality}`)
      return;
    }

  }
}