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
  for(i = 1; i<=298;i++) {
      for(j = 1; j<=298;j++) {
          let maxsq =  300 - ((j < i)? i: j);
          let potential = 0;

          for(z = 3;z < maxsq; z++) {
            for(k = 0;k < z;k++) {
              for(l = 0;l < z; l++) {
                //console.log(i,j,k,l)
              //  console.log(i+k, j+l)
                potential += arr[i + k][j + l];
              }
            }
          }
         //console.log('====')
          
          if(potential > highest) {
              highest = potential;
              highestx = i;
              highesty = j;
              highestsz = maxsq;
          }
      }
  }
  return highestx + ',' + highesty + ',' + highestsz;
}


// Best Grid
console.log(highpower(18) == '90,269,16')
//console.log(highpower(42) == '21,61')
//console.log(highpower(7403))