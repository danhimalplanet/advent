#!/usr/bin/env perl6

use lib $*PROGRAM.parent.child('lib');
use Day03;

sub MAIN(Str $f) {
	my $c = Canvas.new(load => $f.IO.lines);
	say "Part 1: {$c.part1}";

	say "Part 2: {$c.part2}";
}
