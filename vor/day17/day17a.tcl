set max 9
set spin 3

set stage {0}
set current 0

for {set level 1} {$level <= $max} {incr level} {
  puts "current: $current spin: $spin level: $level"

  if {$spin > $level} {
    set remspin [expr {$spin % $level}]
  } else {
    set remspin $spin
  } 

  if {$current + $remspin >= $level} {
      set inpoint [expr {($current + $remspin) - $level}]
  } else {
    set inpoint [expr {$current + $remspin}] 
  }

  set current [expr {$inpoint + 1}]
  linsert $stage $current $level

  puts "insert $level at $current"

}
puts $stage
#search for 2017
#output next index