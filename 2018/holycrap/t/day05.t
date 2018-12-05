use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day05;

plan 2;

say "Part 1";
is part1("dabAcCaCBAcCcaDA"), 10, 'dabAcCaCBAcCcaDA reacts into dabCBAcaDA';

say "Part 2";
is part2("dabAcCaCBAcCcaDA"),  4, 'Shortest possible reaction is 4';

done-testing;
