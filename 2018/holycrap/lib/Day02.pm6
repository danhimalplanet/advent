unit module Day02;

# Categorised based on repetitions (use Unique to avoid classifying something multiple times) and
# simply multiply the numbers with 2 and 3 repeats.
sub part1(@w) is export {[*] @w.categorize({bag(.comb).values.unique}){2,3}}

# Compare each word against each other word, returning as soon as the number of equal letters is the
# inverse of our target number. Zip is used to replace different letters with a 0 length list which
# is elided by join.
sub part2(@w, $t) is export {
	for @w.combinations(2) -> [$a, $b] {
		return zip($a.comb, $b.comb, :with(-> $a, $b { $a eq $b ?? $a !! |() })).join
			if ([+] $a.comb Zeq $b.comb) == $a.chars - $t
	}
}
