set fsize [file size "day18.txt"]
set fp [open "day18.txt" r]
set stream [read $fp $fsize]
close $fp

set stream [split $stream '\n']
for {set x 0} {$x <  [llength $stream]} {incr x} {  

  set line [lindex $stream $x]
  set elements [split $line " "]
  set cmd [lindex $elements 0]
  set target [lindex $elements 1]
  set value [lindex $elements 2]
  array set notes {}

  if {[info exists notes($target)] == 0} {
    set notes($target) 0
  }
  if {[string match {*[A-Z]*} $value] == 1} {
    if {[info exists notes($value)] == 0} {
      set notes($value) 0
    }
    set value $notes($value)
  }
  puts "For: $target Notes: $notes($target) Value: $value"
  puts "seed: notes([join {[$target] s} ""]"

  switch $cmd {
    snd {
      set notes([join {[notes($target)] s} ""]) $value
    }
    set {
      puts "set $target to $value"
      set notes($target) $value
    }
    add {
      incr notes($target) $value
    }
    mul {
      set notes($target) [expr {$notes($target) * $value}]
      puts "multiplied $value to $notes($target)"
    }
    mod {
      set notes($target) [expr {[expr {$notes($target)}] % $value}]
    }
    rcv {
      if {$notes([join {[notes($target)] s} ""]) <> 0} {
        set notes($target) $notes([join {[notes($target)] s} ""])
      }
    }
    jgz {
      if {$notes($target) > 0} {
        incr x $value
      }
    }
  }
}
