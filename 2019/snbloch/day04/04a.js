function hasAdjacent(number) {
    if (number.toString().includes('00') ||
    number.toString().includes('11') ||
    number.toString().includes('22') ||
    number.toString().includes('33') ||
    number.toString().includes('44') ||
    number.toString().includes('55') ||
    number.toString().includes('66') ||
    number.toString().includes('77') ||
    number.toString().includes('88') ||
    number.toString().includes('99')) {
        return true;
    }
    else {
        return false;
    }
}

function isIncreasing(number) {
    for (var i = 0; i < number.toString().length - 1; i++) {
        if (parseInt(number.toString()[i]) > parseInt(number.toString()[i + 1])) {
            return false;
        }
    }
    return true;
}

function main() {
    var count = 0;
    for (var i = 128392; i <= 643281; i++) {
        if (hasAdjacent(i) && isIncreasing(i)) {
            count += 1;
        }
    }
    console.log(count);
}

main();