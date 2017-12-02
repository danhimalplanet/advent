unit module Day2;

# %% returns a bool, it'd be nicer if it returned the division, so do that
sub infix:<%/%> { $^l/$^r if $^l %% $^r }
sub evenly-divisible(@c ($l, $r)) { $l %/% $r or $r %/% $l }

# I'd rather these were in the .p6 but I need to use them from tests too
sub part1 is export {$^l.max - $^l.min}
sub part2 is export {[+] $^l.combinations(2).map: &evenly-divisible}

# Call a Callable on each line after splitting them into a Numeric list
sub process-file(Str $f where *.IO.r, Callable $c) is export {
	$f.IO.lines».split(/\t/)».Numeric.map: $c;
}

