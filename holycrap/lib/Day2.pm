unit module Day2;

# Due to sorting the list in part2, l ≤ r so we need only one test
sub evenly-divisible(@c ($l, $r)) { $r/$l if $r%%$l }

# I'd rather these were in the .p6 but I need to use them from tests too
sub part1 is export {$^l.max - $^l.min}
sub part2 is export {[+] $^l.sort.combinations(2).map: &evenly-divisible}

# Call a Callable on each line after splitting them into a Numeric list
sub process-file(Str $f where *.IO.r, Callable $c) is export {
	$f.IO.lines».words».Numeric.map: $c;
}

