use Test;

use lib $*PROGRAM.parent.parent.child('lib');
use Day04;

plan 2;

my $l = GuardLog.new(load => [
	'[1518-11-01 00:00] Guard #10 begins shift',
	'[1518-11-01 00:05] falls asleep',
	'[1518-11-01 00:25] wakes up',
	'[1518-11-01 00:30] falls asleep',
	'[1518-11-01 00:55] wakes up',
	'[1518-11-01 23:58] Guard #99 begins shift',
	'[1518-11-02 00:40] falls asleep',
	'[1518-11-02 00:50] wakes up',
	'[1518-11-03 00:05] Guard #10 begins shift',
	'[1518-11-03 00:24] falls asleep',
	'[1518-11-03 00:29] wakes up',
	'[1518-11-04 00:02] Guard #99 begins shift',
	'[1518-11-04 00:36] falls asleep',
	'[1518-11-04 00:46] wakes up',
	'[1518-11-05 00:03] Guard #99 begins shift',
	'[1518-11-05 00:45] falls asleep',
	'[1518-11-05 00:55] wakes up']);

say "Part 1";
is $l.part1(),  240, 'Guard #10 slept the most, mostly in minute 24';

say "Part 2";
is $l.part2(), 4455, 'Guard #99 spent minute 45 asleep more than any other guard';

done-testing;
