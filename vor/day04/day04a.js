(function(){
    let aoc = require('../lib/aoc.js')
    let spread = aoc.inputfile('./day04.txt').split('\n')
    let bad, checksum = 0

    spread.forEach(function(element){
        let words = element.split(' ').sort() 

        bad = 0
        aoc.allcompare(words, function(wordA, wordB, indexA, indexB){
            if (bad == 0 && wordA == wordB && indexA != indexB) bad = 1
        })        
        // words.forEach(function(wordA, indexA){
        //     words.forEach(function(wordB, indexB){
        //         console.log(bad, wordA, indexA, wordB, indexB, checksum)
        //         if (bad == 0 && wordA == wordB && indexA != indexB) bad = 1
        //     })    
        // })
        if (bad == 0){
            checksum += 1
        }
    })
    console.log(checksum)
})()