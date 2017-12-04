#!/usr/bin/env perl6
use lib $*PROGRAM.parent.child('lib');
use Day4;

sub MAIN($f where *.IO.r) {
	say "Part 1: Out of {$f.IO.lines.elems} there are {$f.IO.lines.elems - invalid($f.IO.lines)} valid";
	say "Part 2: Out of {$f.IO.lines.elems} there are {$f.IO.lines.elems - invalid_ana($f.IO.lines)} new valid";
}
