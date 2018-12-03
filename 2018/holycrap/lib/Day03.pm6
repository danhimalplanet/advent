unit module Day03;

class Rectangle {
    has Int $.x;
    has Int $.y;
    has Int $.w;
    has Int $.h;
    has int $.depth;
}

grammar Rect {
	token TOP { "#" <num> " @ " <num> "," <num> ": " <num> "x" <num> }
	token num { \d+ }
}

class RectReify {
	method TOP ($/) {
		make Rectangle.new(
			x => $/<num>[1].Int,
			y => $/<num>[2].Int,
			w => $/<num>[3].Int,
			h => $/<num>[4].Int,
		)
	}
}

sub import(@l) {
	# Parse the rectangles from the input file format
	my @rects = @l.map: {Rect.parse($_, actions => RectReify).made};

	# Create simple spatial indexes along X and Y to avoid a grid structure
	my %x;
	my %y;
	for @rects.pairs -> $r {
		($r.value.y ..^ $r.value.y+$r.value.h).map({ %y{$_}.push($r.key) });
		($r.value.x ..^ $r.value.x+$r.value.w).map({ %x{$_}.push($r.key) });
	}

	return %x, %y;
}

sub part1(@l) is export {
	my ($x, $y) = import @l;

	# Iterate all combinations of keys in X and Y, summing any where the intersecting set of
	# rectangle IDs has > 1 elem, i.e more than one rectangle occupies this space on x+y axes
	[+] ($x.keys X $y.keys).map: -> [$a, $b] {
		(set(|$x{$a}) ∩ set(|$y{$b})).elems > 1 ?? 1 !! 0;
	}
}

sub part2(@l) is export {
	my ($x, $y) = import @l;

	# All rectangle IDs that have a non-overlapping position
	my $i = set ($x.keys X $y.keys).map: -> [$a, $b] {
		my $i = set(|$x{$a}) ∩ set(|$y{$b});
		|$i.keys if $i.elems == 1;
	}

	# All rectangle IDs that do overlap
	my $o = set ($x.keys X $y.keys).map: -> [$a, $b] {
		my $i = set(|$x{$a}) ∩ set(|$y{$b});
		|$i.keys if $i.elems > 1;
	}

	1 + ($i (-) $o).keys[0]; # Assume there'll be only one so pick the first
}
