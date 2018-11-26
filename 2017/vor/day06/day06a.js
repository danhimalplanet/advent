let memory = "10  3 15  10  5 15  5 15  9 2 5 8 5 2 3 6"
memory = memory.replace(/[\s]+/g,':').split(':').map( Number)

let banks = 16;
let lastindex = banks - 1
let savestate = [] 

savestate.push(memory.join(""))

for (let i = 1; i < 15000; i++){
    let tmax = Math.max.apply(null, memory);    
    let tmaxindex = memory.indexOf(tmax);

    let tbottom = Math.floor(tmax / banks);
    let tdiff = tmax - (banks * tbottom);

    memory[tmaxindex] = 0;
    let endindex, midindex;

    if ((tdiff + tmaxindex) >= lastindex) {
        endindex = lastindex;
        midindex = (tdiff - (lastindex - tmaxindex) - 1);
    } else {
        endindex = tdiff + tmaxindex;
        midindex = -1;
    }

    for (let x = 0; x < banks; x++) {
        memory[x] += (x < tmaxindex && x <= midindex) || (x > tmaxindex && x <= endindex) ? tbottom + 1 : tbottom;
    }

    let used = savestate.indexOf(memory.join(""))
    if (used != -1) {
        console.log(i);
        break;
    } else {
        savestate.push(memory.join(""))
    }
}