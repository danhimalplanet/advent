let input = 289326
let grid = {}

let total = 0
let layer = 1
let center = 5
let direction = 'right'
let x = center
let y = center
let current = (x * 10) + y
grid[current] = 1

while (total <= input ) {
    switch (direction) {
        case 'right': 
            if (x < (center + layer)) {
                x += 1
            } else {
                direction = 'up'
                y += 1
            }
            break
        case 'up':
            if (y < (center + layer)) {
                y += 1
            } else {
                direction = 'left'
                x -= 1
            }
            break
        case 'left':
            if (x > (center - layer)) {
                x -= 1
            } else {
                direction = 'down'
                y -= 1
            }
            break
        case 'down':
            if (y > (center - layer)) {
                y -= 1
            } else {
                direction = 'right'
                x += 1
                layer += 1
            }       
            break
    }

    current = (x * 10) + y
    total = 0

    // Right
    tindex = ((x + 1) * 10) + y
    total += (grid[tindex] == undefined)? 0 : grid[tindex]

    // Top Right
    tindex = ((x + 1) * 10) + (y + 1)
    total += (grid[tindex] == undefined)? 0 : grid[tindex]

    // Top
    tindex = (x * 10) + (y + 1)
    total += (grid[tindex] == undefined)? 0 : grid[tindex]

    // Top Left
    tindex = ((x - 1) * 10) + (y + 1)
    total += (grid[tindex] == undefined)? 0 : grid[tindex]

    // Left
    tindex = ((x - 1) * 10) + y
    total += (grid[tindex] == undefined)? 0 : grid[tindex]

    // Bottom Left
    tindex = ((x - 1) * 10) + (y - 1)
    total += (grid[tindex] == undefined)? 0 : grid[tindex]

    // Bottom
    tindex = (x * 10) + (y - 1)
    total += (grid[tindex] == undefined)? 0 : grid[tindex]

    // Bottom Right
    tindex = ((x + 1) * 10) + (y - 1)
    total += (grid[tindex] == undefined)? 0 : grid[tindex]

    grid[current] = total 
}
console.log(total)
