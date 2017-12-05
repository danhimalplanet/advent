unit module Day1;

# Return LHS if arguments are numerically equal, is tighter no longer needed
sub infix:<←=> { $^l == $^r ?? $^l !! False }
# Sum any elements of the captcha that match the equivalent element of a rotated list
sub solve-captcha(Str $c, Callable $l={1}) is export {
	[+] $c.comb Z←= $c.comb.list.rotate: $l($c)
}
