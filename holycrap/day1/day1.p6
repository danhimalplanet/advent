#!/usr/bin/env perl6
use Test;

# Return LHS if arguments are numerically equal, is tighter no longer needed
sub infix:<←=> { $^l == $^r ?? $^l !! False }
# Sum any elements of the captcha that match the equivalent element of a rotated list
sub solve-captcha(Str $c, Callable $l={1}) { [+] $c.comb Z←= $c.comb.list.rotate: $l($c) }

sub MAIN(Str $captcha where /^\d+$/) {
	say "Part 1 code answer is {solve-captcha $captcha}";
	say "Part 2 code answer is {solve-captcha $captcha, *.chars/2}";
}

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
