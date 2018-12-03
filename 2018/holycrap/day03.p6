#!/usr/bin/env perl6

use lib $*PROGRAM.parent.child('lib');
use Day03;

sub MAIN(Str $f) {
	my @l = $f.IO.lines;
	say "Part 1: {part1(@l)}";

	say "Part 2: {part2(@l)}";
}
