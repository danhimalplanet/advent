set fsize [file size "day12.txt"]
set fp [open "day12.txt" r]
set pipes [read $fp $fsize]
close $fp

set queue {0 737}
set pipes [split $pipes '\n']
for {set x 0} {$x < [llength $queue]} {incr x} {
  set target [lindex $pipes [lindex $queue $x]]
  set branch [split $target ",>"]
  set j 0
  foreach i $branch {
    if {$j >= 1} {
      set newnum [string trim $i]
      if {[lsearch $queue $newnum] == -1} {
        lappend queue $newnum
      }
    }
    incr j
  }
}
puts [llength $queue]