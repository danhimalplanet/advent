unit module Day05;

# This is an uglier version of the original code I wrote because Perl takes foreeeever to copy a
# 50,000 element long list. Instead we iterate the list once, mutating a target array. Still clean.
sub part1($s) is export {
	my @c = $s.comb.list;
	my @t;

	for @c.keys -> $i {
		((@t.tail and @t.tail eq @t.tail.uc and @c[$i] eq @c[$i].lc and @t.tail.fc eq @c[$i].fc) or
		 (@t.tail and @t.tail eq @t.tail.lc and @c[$i] eq @c[$i].uc and @t.tail.fc eq @c[$i].fc))
			?? @t.pop !! @t.push(@c[$i])
	}
	return @t.join.chars;
}

# Run part 1 with all instances of each particular reacting pair removed, find the shortest
sub part2($s) is export {
	$s.lc.comb.Set.keys.race.map(-> $c {part1 $s.subst(/:i<{$c}>/, '', :g)}).min;
}
