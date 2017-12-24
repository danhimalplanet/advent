set fsize [file size "day18.txt"]
set fp [open "day18.txt" r]
set stream [read $fp $fsize]
close $fp

set stream [split $stream '\n']
array set notes {a 0 b 0 f 0 i 0 p 0 as 0 bs 0 fs 0 is 0 ps 0}
set key {a b f i p}

for {set x 0} {$x <  [llength $stream] } {incr x} {  

  set line [lindex $stream $x]
  set elements [split $line " "]
  set cmd [lindex $elements 0]
  set target [lindex $elements 1]
  set value [lindex $elements 2]
  set note [concat [expr {$target}]s]

  if {[regexp {[a-z]+} $value] == 1} {
    set value $notes($value)
  } 

  if {[regexp {[0-9]+} $target]} {
    set target [lindex $key $target]
    set note [concat [expr {$target}]s]
  }
  
  switch $cmd {
    snd {
      set notes($note) $notes($target)
    }
    set {
      set notes($target) $value
    }
    add {
      set notes($target) [expr {$notes($target) + $value}]
    }
    mul {
      set notes($target) [expr {$notes($target) * $value}]
    }
    mod {
      set notes($target) [expr {$notes($target) % $value}]
    }
    rcv {
      if {$notes($note) != 0} {
      puts "$notes($note)"
      break
      }
    }
    jgz {
      if {$notes($target) != 0} {
        incr x [expr {$value - 1}]
      }
    }
  }
}
