unit module Day05;

# This is an uglier version of the original code I wrote because Perl takes foreeeever to copy a
# 50,000 element long list. Instead we iterate the list once, mutating a target array. Still clean.
sub part1($s) is export {
	my @c = $s.comb.list;
	my @t;

	for @c.values -> $c {
		(@t.tail and (@t.tail.fc eq $c.fc) and (
			(@t.tail eq @t.tail.uc  and  $c eq $c.lc) or
			(@t.tail eq @t.tail.lc  and  $c eq $c.uc)))
				?? @t.pop !! @t.push($c)
	}
	@t.join.chars;
}

# Run part 1 with all instances of each particular reacting pair removed, find the shortest
sub part2($s) is export {
	$s.lc.comb.Set.keys.race.map(-> $c {part1 $s.subst(/:i<{$c}>/, '', :g)}).min;
}
