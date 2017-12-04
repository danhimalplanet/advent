unit module Day4;

sub invalid    ($l) is export { $l».words».Bag.grep: *.values.grep(*>1) }
sub invalid_ana($l) is export { $l».words».map(*.comb.sort.join)».Bag.grep: *.values.grep(*>1) }
