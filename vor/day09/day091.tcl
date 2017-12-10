set fsize [file size "day09.txt"]
set fp [open "day09.txt" r]
set stream [read $fp $fsize]
close $fp

set total 0
set stream [expr {[string map {\!> #} [expr {$stream}]]}]
set stream [expr {[string map {\!\! z} [expr {$stream}]]}]
set stream [expr {[string map {\!# >} [expr {$stream}]]}]
regsub -all {<([^>]+)?>|,} $stream {} stream
puts $stream

#1. find max level
set max_level 9

#for each level from max_level to 0
  set step [expr {$max_level - 1}]

  # $count {} within the current step
  # (?<=[,}][\{]{$step})({})

  # Add ($count * $max_level)

  # Remove {} from this level

# loop down a level

# puts #total