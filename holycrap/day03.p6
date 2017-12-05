#!/usr/bin/env perl6
use lib $*PROGRAM.parent.child('lib');
use Day3;

sub MAIN (Int $num) {
	my $s = NumberShape.new(layers => (1,8,*+8…*), sides => 4);

	# Part 1
	say "Distance to centre: {$s.to-centre(|$s.descend($num))}";

	# Part 2
	say "First item over limit: {$s.generate($num)[0]}";
}
