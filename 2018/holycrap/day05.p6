#!/usr/bin/env perl6

use lib $*PROGRAM.parent.child('lib');
use Day05;

sub MAIN(Str $f) {
	my $i = $f.IO.lines.first;
	say "Part 1: {part1($i)}";

	say "Part 2: {part2($i)}";
}
