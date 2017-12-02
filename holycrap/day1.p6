#!/usr/bin/env perl6
use lib 'lib';
use Day1;

sub MAIN(Str $captcha where /^\d+$/) {
	say "Part 1 code answer is {solve-captcha $captcha}";
	say "Part 2 code answer is {solve-captcha $captcha, *.chars/2}";
}
