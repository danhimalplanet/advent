use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day3;

plan 9;

my $s = NumberShape.new(layers => (1,8,*+8…*), sides => 4);

say "Part 1";
is $s.to-centre(|$s.descend(   1)),  0, "   1 = 0";
is $s.to-centre(|$s.descend(  12)),  3, "  12 = 3";
is $s.to-centre(|$s.descend(  23)),  2, "  23 = 2";
is $s.to-centre(|$s.descend(1024)), 31, "1024 =31";

say "Part 2";
my @spiral = |$s.generate(10)[1];
is @spiral[0][0], 1, "Square 1 = 1";
is @spiral[1][0], 1, "Square 2 = 1";
is @spiral[1][1], 2, "Square 3 = 2";
is @spiral[1][2], 4, "Square 4 = 4";
is @spiral[1][3], 5, "Square 5 = 5";

done-testing;

