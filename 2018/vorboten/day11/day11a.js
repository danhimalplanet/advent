//const serial = 7403;

powerup = (x, y, serial) => {
    let power = ((y * (x + 10)) + serial) * (x + 10);
    return ((power >= 100)? Math.floor((power % 1000) / 100): 0) -5;
}

grid = (serial) => {
    let arr = Array.from(Array(301), () => new Array(301));
    for(i = 1; i<=300;i++) {
        for(j = 1; j<=300;j++) {
            arr[i][j] = powerup(i, j, serial);
        }
    }
    return arr;
}

highpower = (serial) => { 
    let highest = 0,
        highestx,
        highesty;
    let arr = grid(serial);
    for(i = 1; i<=297;i++) {
        for(j = 1; j<=297;j++) {
            let maxsq = 3;
            let potential = 0;
            for(k = 1;k <= maxsq;k++) {
                    console.log('-: ', i, j, k)
                    potential += sumcol(arr, i,j,k)
                    potential += sumrow(arr, j,i,k - 1)               
            }
            
            if(potential > highest) {
                highest = potential;
                highestx = i;
                highesty = j;
            }
        }
    }
    return highestx + ',' + highesty
}


sumcol = (arr, colno, start, items) => {
    let colsum = 0;
    if(items > 0) {
        for(i = start; i <= (start + items - 1); i++) {
            colsum += arr[colno][i];
          }      
    }
    console.log('c: ',colno, start, items, colsum)
    return colsum;
}


sumrow = (arr, rowno, start, items) => {
    let rowsum = 0;
    if(items > 0) {
        for(i = start; i <= (start + items); i++) {
        rowsum += arr[i][rowno];
        }
    }
    console.log('r: ',rowno, start, items, rowsum)
    return rowsum;
}



// // Power calculation
// console.log(powerup(3, 5, 8) == 4);
// console.log(powerup(122, 79, 57) == -5);
// console.log(powerup(217, 196, 39) == 0);
// console.log(powerup(101, 153, 71) == 4);

// Best Grid
console.log(highpower(18) == '33,45')
// console.log(highpower(42) == '21,61')
// console.log(highpower(7403))