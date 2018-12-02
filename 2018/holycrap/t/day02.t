use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day02;

plan 2;

say "Part 1";
is part1(<abcdef bababc abbcde abcccd aabcdd abcdee ababab>), 12, 'Checksum code is 12';

say "Part 2";
is part2(<abcde fghij klmno pqrst fguij axcye wvxyz>), 'fgij', 'Box ID is fgij';

done-testing;
