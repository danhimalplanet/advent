unit module Day03;

grammar Rect {
	token TOP { "#" <num> " @ " <num> "," <num> ": " <num> "x" <num> }
	token num { \d+ }
}

class Rectangle {
	has Int $.id;
	has Int $.x;
	has Int $.y;
	has Int $.w;
	has Int $.h;
}

class RectReify {
	method TOP ($/) {
		make Rectangle.new(
			id => $/<num>[0].Int,
			x  => $/<num>[1].Int,
			y  => $/<num>[2].Int,
			w  => $/<num>[3].Int,
			h  => $/<num>[4].Int,
		)
	}
}


class Canvas is export {
	has Rectangle %.rects{Int};
	has %.x;
	has %.y;

	submethod BUILD(:@load) {
		# Load every input line and transform into a real object using grammar/actions above
		my @r = @load.map: {Rect.parse($_, actions => RectReify).made};

		# Bind the real object by index. Sink required as these are side effects
		sink @r.map: {%!rects{.id} := $_};

		# Categorise each rectangle into the X and Y space it takes up, forming sets of their ids
		%!x = @r.categorize({.x ..^ .x+.w}).pairs.race.map: {.key => set(|.value».id)};
		%!y = @r.categorize({.y ..^ .y+.h}).pairs.race.map: {.key => set(|.value».id)};
	}

	# Iterate all combinations of keys in X and Y, summing any where the intersecting set of
	# rectangle IDs has > 1 elem, i.e more than one rectangle occupies this space on x+y axes
	method part1 {
		[+] (%!x.keys X %!y.keys).race.map: -> [$a, $b] { (%!x{$a} ∩ %!y{$b}).elems > 1 }
	}

	# Iterate all combinations again but keep track of two sets. Those IDs which appear on their
	# own, and those IDs which appear with others.
	method part2 {
		my ($s, $m) = set(), set(); # Single and Multi appearances

		(%!x.keys X %!y.keys).race.map: -> [$a, $b] {
			given %!x{$a} ∩ %!y{$b} {
				when .elems == 1 { $s = $s ∪ $_ }
				when .elems  > 1 { $m = $m ∪ $_ }
			}
		}

		# Subtract those seen with others from those seen on their own
		$s (-) $m;
	}
}
