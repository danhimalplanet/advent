use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day5;

plan 2;

my @maze = <0 3 0 1 -3>».Int;

say "Part 1";
is escape(@maze), 5, "Escaped maze in 5 steps";

say "Part 2";
is escape(@maze, &move-p2), 10, "Escaped maze in 10 steps";

done-testing;


