const aoc = require('../lib/aoc.js');
const boxes = inputfile('./day02.txt', true);

let boxlist = new Set();
const result =  boxes.forEach(box =>{
  for (let char of String.prototype.concat(...new Set(box))) {
    regex = new RegExp(char, "g");
    if(box.match(regex) && (box.match(regex).length === 2 ||  box.match(regex).length === 3)) boxlist.add(box);
  }
})

let boxlist2 = boxlist;
for (let box of boxlist) {
  boxlist2.delete(box);
  for(let box2 of boxlist2) {
    for(i = 0;i < box.length; i++) {
      if(box.charAt(i) != box2.charAt(i) ) {
        if(box.substring(i + 1, box.length) === box2.substring(i + 1, box2.length)) {
          console.log(box.substring(0, i) + box.substring(i + 1, box.length));
          break;
        } else {
          i = box.length;
        }      
      }
    }
  }
}