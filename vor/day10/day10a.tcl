set fsize [file size "day10.txt"]
set fp [open "day10.txt" r]
set instructions [read $fp $fsize]
close $fp

set listsize 256
set circle {0}
set current 0
set offset 0

for {set x 1} {$x < $listsize} {incr x} { lappend circle $x }
set instructions [expr {[split $instructions ',']}]

foreach steps $instructions {
	set steps_to_end [expr {$listsize - $current}]
	set remainder [expr {$steps - $steps_to_end}]
	set frontstop [expr {$remainder - 1}]
	set endstop [expr {$current + ($steps - 1)}]

	set endlist [expr {[lrange $circle $current $endstop]}]

	if {$remainder > 0} {
		set frontlist [expr {[lrange $circle 0 $frontstop]}]
		set endlist [expr {[concat $endlist $frontlist]}]
	}

	foreach j [expr {[lreverse $endlist]}] {
		lset circle $current $j
		if {($current + 1) >= $listsize} {
			set current 0
		} else {
			set current [expr {$current + 1}]
		}
	}
	if {$current + $offset >= $listsize} {
		set current [expr {($offset + $current) - $listsize}]
	} else {
		set current [expr {$current + $offset}]
	}
	incr offset

}
puts [expr {[lindex $circle 0] * [lindex $circle 1]}]

