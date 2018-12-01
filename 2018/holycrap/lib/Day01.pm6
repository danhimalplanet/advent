unit module Day01;

# For part 1 we just sum the list we're given
sub part1 is export {[+] @_}

# For part 2 we make an infinite sequence adding as we go, then return a list of those elements
# that repeat. Because it's lazy and the caller only gets the first element, only that is calculated
sub part2 is export {([\+] |@_ xx *).repeated}
