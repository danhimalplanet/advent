set fsize [file size "day18.txt"]
set fp [open "day18.txt" r]
set stream [read $fp $fsize]
close $fp

set stream [split $stream '\n']
for {set x 0} {$x <  [llength $stream]} {incr x} {  
set line [lindex $stream $x]
  puts $line
  set elements [split $line " "]
  set cmd [lindex $elements 0]
  set target [lindex $elements 1]
  set value [lindex $elements 2]

  switch $cmd {
    snd {
      set xS $value
    }
    set {
      set $target $value
      puts $$target
    }
    add {
      set $target [$$target + $value]
    }
    mul {
      set $target [$$target * $value]
    }
    mod {
      set $target [$$target & $value]
      puts mod
    }
    rcv {
      if {xS <> 0} {
        set $target $xS
      }
    }
    jgz {
      if {$$target > 0} {
        incr x $value
      }
    }
  }

}
