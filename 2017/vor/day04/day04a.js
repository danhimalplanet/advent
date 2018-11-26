(() => {
    let aoc = require('../lib/aoc.js');
    let spread = aoc.inputfile('./day04.txt', true);
    let bad, checksum = 0;

    spread.forEach((element) => {
        let words = element.split(' ').sort();
        bad = 0;
        aoc.allcompare(words, (wordA, wordB, indexA, indexB) => {
            if (bad == 0 && indexA != indexB && wordA == wordB) bad = 1;
        }) 
        if (bad == 0) checksum += 1;
    });
    console.log(checksum);
})()