unit module Day02;

# Categorised based on repetitions (use Unique to avoid classifying something multiple times) and
# simply multiply the numbers with 2 and 3 repeats.
sub part1(@w) is export {[*] @w.categorize({bag(.comb).values.unique}){2,3}}

# Compare each word against each other word, returning as soon as the number of equal letters is the
# inverse of our target number.
sub part2(@w, $t) is export {
	for @w.combinations(2) -> [$a, $b] {
		if ([+] $a.comb Zeq $b.comb) == $a.chars - $t {
			return zip($a.comb, $b.comb, :with({$^a if $^a eq $^b})).join
		}
	}
}
