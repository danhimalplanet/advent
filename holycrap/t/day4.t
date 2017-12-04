use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day4;

plan 8;

say "Part 1";
is   invalid(['aa bb cc dd ee']).elems,  0, 'aa bb cc dd ee  == valid';
isnt invalid(['aa bb cc dd aa']).elems,  0, 'aa bb cc dd aa  == invalid';
is   invalid(['aa bb cc dd aaa']).elems, 0, 'aa bb cc dd aaa == valid';

say "Part 2";
is   invalid_ana(['abcde fghij']).elems,              0, 'abcde fghij              == valid';
isnt invalid_ana(['abcde xyz ecdab']).elems,          0, 'abcde xyz ecdab          == invalid';
is   invalid_ana(['a ab abc abd abf abj']).elems,     0, 'a ab abc abd abf abj     == valid';
is   invalid_ana(['iiii oiii ooii oooi oooo']).elems, 0, 'iiii oiii ooii oooi oooo == valid';
isnt invalid_ana(['oiii ioii iioi iiio']).elems,      0, 'oiii ioii iioi iiio      == invalid';

done-testing;


