#!/usr/bin/env perl6

use lib $*PROGRAM.parent.child('lib');
use Day01;

sub MAIN(Str $f) {
	say "Part 1: {part1($f.IO.lines)}";

	say "Part 2: {part2($f.IO.lines)[0]}";
}
