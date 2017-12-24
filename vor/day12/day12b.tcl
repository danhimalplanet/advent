set fsize [file size "day12.txt"]
set fp [open "day12.txt" r]
set pipes [read $fp $fsize]
close $fp

# Search for first not in queue -- if none break
# loop using that as beginning
# incr queuecount

set queue {0}
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
puts [lsort $queue]
puts [llength $queue]