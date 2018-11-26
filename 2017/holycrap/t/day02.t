use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day2;

plan 6;

say "Part 1";
is part1(<5 1 9 5>), 8, "5 1 9 5 = 8";
is part1(  <7 5 3>), 4, "  7 5 3 = 4";
is part1(<2 4 6 8>), 6, "2 4 6 8 = 6";

say "Part 2";
is part2(<5 9 2 8>), 4, "5 9 2 8 = 4";
is part2(<9 4 7 3>), 3, "9 4 7 3 = 3";
is part2(<3 8 6 5>), 2, "3 8 6 5 = 2";

done-testing;
