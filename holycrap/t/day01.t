use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day1;

plan 9;

say "Part 1";
is solve-captcha(    '1221'), 3, "    1221 = 3";
is solve-captcha(    '1111'), 4, "    1111 = 4";
is solve-captcha(    '1234'), 0, "    1234 = 0";
is solve-captcha('91212129'), 9, "91212129 = 9";

say "Part 2";
is solve-captcha(    '1212', *.chars/2),  6, "    1212 = 6";
is solve-captcha(    '1221', *.chars/2),  0, "    1221 = 0";
is solve-captcha(  '123425', *.chars/2),  4, "  123425 = 4";
is solve-captcha(  '123123', *.chars/2), 12, "  123123 =12";
is solve-captcha('12131415', *.chars/2),  4, "12131415 = 4";

done-testing;
