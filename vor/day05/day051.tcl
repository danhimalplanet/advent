set fsize [file size "day05.txt"]
set fp [open "day05.txt" r]
set chain [read $fp $fsize]
close $fp

set links [split $chain '\n']
set last [expr {[llength $links]}]
set indicy 0
for {set x 1} {$x == $x} {incr x} {
  set current [lindex $links $indicy]
  set links [lset links $indicy [expr {$current + 1}]]
  set indicy [expr {$indicy + $current}]
  if {$indicy < 0 || $indicy >= $last} {
    puts "Steps: $x"
    break
  }
}


