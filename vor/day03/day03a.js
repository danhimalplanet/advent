(function(){
    let input = 289326
    let runner = Math.round(Math.sqrt(input));
    let lower = (runner * (runner - 1)) + 1
    let higher = runner * (runner + 1)
    let ldiff = input - lower
    let hdiff = higher - input

    var x, y
    if (runner % 2 == 0) {        
        if (input <= (higher - runner)) {
            x = runner / 2
            y = (runner / 2) - ldiff
        } else {
            x = (0 - ((runner / 2) - 1)) + hdiff
            y =  0 - (runner / 2)
        }
    } else {
        if (input <= (higher - runner)) {       
            x = (0 - (runner - 1 )) / 2
            y = (0 - (runner / 2)) + ldiff
        } else {
            x = ((runner - 1 ) / 2) - hdiff
            y = ((runner - 1 ) / 2) + 1
        }
    }
    output = Math.abs(x) + Math.abs(y)
    console.log(output)
})()