#!/usr/bin/env perl6

use lib $*PROGRAM.parent.child('lib');
use Day2;

sub MAIN(Str $f) {
	say "Part 1: {[+] process-file($f, &part1)}";
	say "Part 2: {[+] process-file($f, &part2)}";
}
