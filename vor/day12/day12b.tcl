set fsize [file size "day12.txt"]
set fp [open "day12.txt" r]
set pipes [read $fp $fsize]
close $fp

# Search for first not in queue -- if none break
# loop using that as beginning
# incr queuecount


set pipes [split $pipes '\n']
set queuecount 0
# [llength $pipes]
for {set x 0} {$x < [llength $pipes]} {incr x} {
  set line [lindex $pipes $x]
  if {$line != {d}} {
    incr queuecount
    set queue [lindex [split $line " ,<->"] 0]
    for {set y 0} {$y < [llength $queue]} {incr y} {
      set target [lindex $pipes [lindex $queue $y]]
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
      lset pipes [lindex $queue $y] d
    }
  }
}
puts $queuecount