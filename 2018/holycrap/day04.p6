#!/usr/bin/env perl6

use lib $*PROGRAM.parent.child('lib');
use Day04;

sub MAIN(Str $f) {
	my $l = GuardLog.new(load => $f.IO.lines);
	say "Part 1: {$l.part1}";

	say "Part 2: {$l.part2}";
}
