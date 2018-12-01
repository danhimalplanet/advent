use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day01;

plan 9;

say "Part 1";
is part1(<1 -2 3 1>), 3, "1 -2 3 1 = 3";
is part1(<1 1 1>),    3, "   1 1 1 = 3";
is part1(<1 1 -2>),   0, "  1 1 -2 = 0";
is part1(<-1 -2 -3>),-6, "-1 -2 -3 =-6";

say "Part 2";
is part2(<1 -2 3 1>)[0],      2, "    1 -2 3 1 =  2";
is part2(<1 -1>)[0],          0, "        1 -1 =  0";
is part2(<3 3 4 -2 -4>)[0],  10, " 3 3 4 -2 -4 = 10";
is part2(<-6 3 8 5 -6>)[0],   5, " -6 3 8 5 -6 =  5";
is part2(<7 7 -2 -7 -4>)[0], 14, "7 7 -2 -7 -4 = 14";
#
done-testing;
