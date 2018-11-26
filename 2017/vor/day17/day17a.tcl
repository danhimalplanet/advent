set max 2017
set spin 366

set stage {0}
set current 0

for {set level 1} {$level <= $max} {incr level} {

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
  set stage [linsert $stage $current $level]
}
puts [lindex $stage [expr {[lsearch $stage 2017] + 1}]]