unit module Day3;

subset Positive of Int where *≥0;

# The grid can be thought of as a number of layers
# 0.  2  3  4  5  6  7  8  9                           (Total 8)
# 1. 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25   (Total 16)
# 2. …

multi sub lower(4,  0, $length, $pos, $side) { 0 } # Only ever retrieve one entry from centre
multi sub lower(4, $l, $length, $pos, $side) {
	((-2..0) »+» ($pos + $length×$side))               # From relative index -1 to 1
		.grep($length×$side-1 ≤ * < $length×($side+1)) # Except where the result is not on the same side
}

sub square($sides, $l, $p, @layers, $pos, $side) {
	# Because this is an advancing spiral, the only values we need to include are
	# 1. The previous number in the sequence
	my @values = -1 => -1,;
	
	# 2. If we are the first on an edge, the second previous number
	@values.push(-1 => -2) unless $pos > 0;

	# 3. The first generated value if we are at the penultimate or ultimate entry
	@values.push(-1 => 0) if $p ≥ @layers[$l]-2;

	# 4. Values from the previous layer
	@values.push(|lower(4, $l-1, @layers[$l-1] div 4, $pos, $side).map: { $l-1 => $_ });
}

class NumberShape is export {
	has Positive $.sides;
	has @.layers;

	multi method side-length( 0) { 1 }; # The bottom layer is special as it is not a polygon
	multi method side-length($l) { @!layers[$l] div $!sides };

	# Split the layer into appropriate sides and return the number's position
	method split($n, $l) { my $s = self.side-length($l); $n mod $s, $n div $s }

	method descend(Positive $n) {
		my Positive $i = $n-1; # Positions really start at 0
		my $layer = 0; # Layers also start at 0
		my @l = @!layers; # Local copy so we can just shift

		try { loop { $i -= shift @l; $layer++ } } # Consume layers until i would become negative

		$layer, self.split($i, $layer)[0]
	}

	multi method to-centre( 0, $n) { 0 } # The bottom layer is special as it is not a polygon
	multi method to-centre($l, $n) { $l + abs(self.side-length($l)[0] div 2 - $n - 1) }

	method generate(Positive $lim, Callable $c=&square) {
		my @generated=[1,],;

		# Ignore the lowest layer
		for 1..* -> $i {
			push @generated, []; # Add our layer

			for ^@!layers[$i] -> $p {
				# Retrieve items from generated list by generating indexes using passed-in function
				my $layer = @generated.end;
				my $sum = [+] (
 	 	 	 	 	$c($!sides, $layer, $p, @!layers, |self.split($p, $layer))
					==> map({ @generated.rotate($^v.key)[0].rotate($^v.value)[0] })
					==> grep(*.defined)
				);
				return $sum, @generated if ($sum > $lim);

				push @generated[*-1], $sum;
			}
		}
	}
}
