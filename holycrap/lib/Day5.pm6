unit module Day5;

sub move($v is rw) { $v++ }

proto move-p2($v is rw) is export {*}
multi move-p2($v is rw where *≥3) { $v-- }
multi move-p2($v is rw)           { $v++ }

sub escape(@maze, Callable $m=&move) is export {
	my @m    = @maze;
	my $p    = 0;
	my $step = 0;

	loop {
		say "Step $step" unless ($step % 100000);

		last unless @m[$p]:exists;
		$p += $m(@m[$p]); $step++
	}
	return $step;
}
