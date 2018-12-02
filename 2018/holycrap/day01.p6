#!/usr/bin/env perl6

use lib $*PROGRAM.parent.child('lib');
use Day01;

sub MAIN(Str $f) {
	my int @l = $f.IO.lines».Int;
	say "Part 1: {part1(|@l)}";

	say "Part 2: {part2(|@l)[0]}";
}
