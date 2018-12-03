use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day03;

plan 2;

say "Part 1";
is part1([
	'#1 @ 1,3: 4x4',
	'#2 @ 3,1: 4x4',
	'#3 @ 5,5: 2x2',
]), 4, '4 Spaces Overlap';

say "Part 2";
is part2([
	'#1 @ 1,3: 4x4',
	'#2 @ 3,1: 4x4',
	'#3 @ 5,5: 2x2',
]), 3, 'Claim 3 does not overlap';

done-testing;
