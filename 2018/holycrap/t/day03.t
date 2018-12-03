use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day03;

plan 2;

my $c = Canvas.new(load => [
	'#1 @ 1,3: 4x4',
	'#2 @ 3,1: 4x4',
	'#3 @ 5,5: 2x2']);

say "Part 1";
is $c.part1(), 4, '4 Spaces Overlap';

say "Part 2";
is $c.part2(), 3, 'Claim 3 does not overlap';

done-testing;
