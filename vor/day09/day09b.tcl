set fsize [file size "day09.txt"]
set fp [open "day09.txt" r]
set stream [read $fp $fsize]
close $fp

set layer 1
set total 0
set streamlen [string length $stream]
set toggleopen false
set garbage false 
set gbgtotal 0

for {set x 0} {$x < $streamlen} {incr x} {
  set currentchar [string index $stream $x]

  switch $currentchar {
    \! {
      incr x
    }
    \< {
      if {!$garbage} {
        set garbage true
      } elseif {$garbage} {
        incr gbgtotal
      }
    }
    \> {
      if {$garbage} {
        set garbage false
      }
    }
    \{ {
      if {$toggleopen && !$garbage} {
        incr layer
        incr total $layer
      } elseif {!$toggleopen && !$garbage} {
        incr total $layer
        set toggleopen true
      } elseif {$garbage} {
        incr gbgtotal
      }
    }
    \} {
      if {$toggleopen && !$garbage} {
          set toggleopen false
      } elseif {!$toggleopen && !$garbage} {
          incr layer -1      
      } elseif {$garbage} {
        incr gbgtotal
      }
    }
    default {
      if {$garbage} {
        incr gbgtotal
      }

    }
  }
}
puts $gbgtotal