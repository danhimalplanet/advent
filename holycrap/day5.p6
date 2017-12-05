#!/usr/bin/env perl6
use lib $*PROGRAM.parent.child('lib');
use Day5;

sub MAIN($f where *.IO.r) {
	my @maze = $f.IO.lines».Int; # Coerce so ++ treats these numerically

	say "Escaped part 1 at step {escape(@maze)}";
	say "Escaped part 2 at step {escape(@maze, &move-p2)}";
}
