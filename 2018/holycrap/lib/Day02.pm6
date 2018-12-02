unit module Day02;

# Categorised based on repetitions (use Unique to avoid classifying something multiple times) and
# simply return the number with 2 and 3 repeats, :v required to not return undefined values
sub part1 is export {
	my $c = categorize { bag(.comb).values.unique }, @_;
	[*] $c{2}:v.elems, $c{3}:v.elems;
}

sub part2(@w) is export {
	# Split the incoming strings into characters, then zip them so they become a list where each
	# element is a character from each string, first characters in element 0, second chars in 1 etc
	# Then construct a hash associating identical characters with an array of their list indexes
	# (which implicitly are indexes in the input list of strings)
	my @c = zip(@w».comb).map: {.pairs.classify({$_.value}, :as{$_.key})};

	# Store a list of differences where each element is a list of difference # with other elements
	my %d{Int} = @w.keys.map: {$_ => [0 xx @w.elems]};

	# For each character, iterate each string, record any not in the 'identical character' list
	for @c.keys -> $j {
		for ^%d.keys -> $i {
			# String indexes that aren't in the list of indexes with the same character
			(set(%d.keys) (-) set(|@c[$j]{substr(@w[$i], $j, 1)})).map: {%d{$_.key}[$i]++};
		}
	}

	# Look through the recorded differences for any that have exactly one with a difference of 1
	my $same = %d.grep({one(|$_.value) == 1}).map(*.key).map: {@w[$_].comb};
	zip(|$same, :with(-> $a, $b { $a eq $b ?? $a !! |() })).join;
}
