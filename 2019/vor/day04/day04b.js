const aoc = require('../lib/aoc.js');
const dictlow = 367479;
const dicthigh = 893698;
let valid = new Set();

processpassword = magic => {
    magic = String(magic)
    digits = [...magic];
    if(digits[0] <= digits[1]
        && digits[1] <= digits[2]
        && digits[2] <= digits[3]
        && digits[3] <= digits[4]
        && digits[4] <= digits[5]
        && ( magic.split(digits[0]).length == 3 
        ||  magic.split(digits[1]).length == 3 
        ||  magic.split(digits[2]).length == 3 
        ||  magic.split(digits[3]).length == 3 
        ||  magic.split(digits[4]).length == 3 
        ||  magic.split(digits[5]).length == 3 
        ||  magic.split(digits[6]).length == 3 )) {
            valid.add(magic)
    }    
}

for(i = dictlow; i <= dicthigh; i++) {
    processpassword(i)
}
console.log(valid.size)