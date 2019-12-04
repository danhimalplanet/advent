const aoc = require('../lib/aoc.js');
const wires = inputfile('./day03.txt');

plotwire = (pair, index) => {
    wire = pair[index].split(',')
    let wirepath = new Set(),
    x = 0,
    y = 0,
    closest = false;
    wire.forEach(plot => {
        direction = plot.charAt(0);
        distance = parseInt(plot.substr(1));
        for(i=0; i < distance; i++) {
            switch(direction) {
            case 'R':
                x++
                break;
            case 'L':
                x--
                break;
            case 'D':
                y++
                break;
            case 'U':
                y--    
                break;
            }
            wirepath.add(x + 'x' + y);
        }
    })
    return wirepath
}

findpath = (match) => {
    plot = match.split('x')
    x = parseInt(plot[0])
    y = parseInt(plot[1])
    return Math.abs(x) + Math.abs(y);
}

processwires = pair => {
    wirepath = plotwire(pair, 0);  
    wirepath2 = plotwire(pair, 1);
    let closest;
    [...wirepath]
        .filter(a => {return wirepath2.has(a)})
        .forEach(match => { if(!closest || findpath(match) < closest) closest = findpath(match) })
    return closest;
}

console.log(processwires(wires))
