set fsize [file size "day13.txt"]
set fp [open "day13.txt" r]
set levels [read $fp $fsize]
close $fp

set levels [split $levels "\n"]
set total 0

for {set x 0} {$x < [llength $levels]} {incr x} {
  set level [lindex $levels $x]
  set step [lindex [split $level ":"] 0]
  set height [string trim [lindex [split $level ":"] 1]]
  set full [expr {(2 * $height) - 2}]
  if {$step > $full} {
    set remstep [expr {$step % $full}]
  } else {
    set remstep $step
  }
  if {$remstep >= $height} {
      set round [expr {($height - 1) - ($remstep - ($height - 1))}]
    } else {
      set round $remstep
    }
  if {$round == 0} {
    incr total [expr {$height * $step}]
  }
}
puts $total