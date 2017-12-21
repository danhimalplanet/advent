set fsize [file size "day19.txt"]
set fp [open "day19.txt" r]
set routes [read $fp $fsize]
close $fp

set line 0
set index 0
set stringscollected ""
set direction "down"
set currentchar "|"

regsub -all " " $routes "@" routes
set routes [split $routes "\n"]
set index [string first $currentchar [lindex $routes $line]]
set toggle false

while {[expr {[string match "A" $currentchar]}] == 0} {
	while {[expr {[string match "+" $currentchar]}] == 0 || $toggle} {
		switch $direction {
			down { 
				incr line 1
			}
			up {
				incr line -1
			}
			right {
				incr index 1
			}
			left {
				incr index -1
			}
		}

		set currentchar [string index [lindex $routes $line] $index]
		if {[string match {*[A-Z]*} $currentchar] == 1} {
			append stringscollected $currentchar
			if {$currentchar eq "A"} {
				break
			}
		}
		set toggle false
	}
	switch $direction {
		down -
		up {
			set next [string index [lindex $routes $line] [expr {$index + 1}]]
			set next [expr {[string match "@" $next] == 1} ? {"left"} : {"right"} ]
			set toggle true
		}
		right -
		left {
			set next [string index [lindex $routes [expr {$line + 1}]] $index]
			set next [expr {[string match "@" $next] == 1} ? {"up"} : {"down"} ]
			set toggle true
		}
	}
	set direction $next
}
puts $stringscollected
