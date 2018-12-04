unit module Day04;

grammar Log {
	token TOP      { '[' <datetime> '] ' <log> }
	token datetime { <num> '-' <num> '-' <num> ' ' <num> ':' <num> }
	token num      { \d+ }
	token log      { .* }
}

class LogCreate {
	method TOP($/)      { make $/<datetime>.made => $/<log> }
	method datetime($/) { make DateTime.new(|%(flat(<year month day hour minute> Z, $/<num>))) }
}

class GuardLog is export {
	# Sleep dictionary, each key is a guard ID, each value is an array of their sleeps, each of
	# which are pairs of start => end
	has %.s;

	submethod BUILD(:@load) {
		%!s.push: gather for @load.map({Log.parse($_, :actions(LogCreate)).made}).sort(*.key) ->$r {
			state ($guard, $start);
			given $r.value {
				when /'Guard #'(\d+)/ { $guard = $/[0] }
				when /'falls asleep'/ { $start = $r.key }
				when /'wakes up'/     { take $guard => ($start => $r.key) }
			}
		}
	}
	method part1 {
		# Classify the list of guards by summed length of sleeps, sort them by that length,
		# selecting the longest. Then take the first guard that slept that long
		my $sleepy = %!s.classify({[+] .value.map: {.value - .key}}).sort(*.key)[*-1].value[0].key;

		# Now categorise their sleeps by the range of minutes they take up. Sleeps are always within
		# the hour so a naive minute range is actually fine. Multiply by sleepy guard's ID.
		$sleepy × %!s{$sleepy}.categorize(
			{$_.key.minute ..^ $_.value.minute}).sort(*.value.elems)[*-1].key;
	}

	method part2 {
		# Categorise sleeper IDs by the minutes they are asleep within. The same naive minute range
		# works here, but it is flattened and slipped so every value within that range is added as a
		# category.
		# The antipairs of this categorisation are [GuardIDs] => minute #, by creating a Bag of the
		# IDs we can sort which GuardID occurred the most frequently
		my $frequent = %!s.keys.categorize(-> $id {
			%!s{$id}.map({ |(.key.minute ..^ .value.minute).flat })
		}).antipairs.map({
			# Output is the minute => the largest pair of GuardID => count.
			.value => bag(.key.values).sort(*.value)[*-1];
		}).sort(*.value.value)[*-1]; # Sort by the count attribute, returning the last

		# The minute number, multiplied by the Guard ID
		$frequent.key × $frequent.value.key
	}
}
