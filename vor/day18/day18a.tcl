set fsize [file size "day18.txt"]
set fp [open "day18.txt" r]
set stream [read $fp $fsize]
close $fp

array set notes {a 0 b 0 f 0 i 0 p 0 as 0 bs 0 fs 0 is 0 ps 0}

set stream [split $stream '\n']
puts "======================"
for {set x 0} {$x <  [llength $stream]} {incr x} {  

  set line [lindex $stream $x]
  set elements [split $line " "]
  set cmd [lindex $elements 0]
  set target [lindex $elements 1]
  set value [lindex $elements 2]
  set note [concat [expr {$target}]s]

  if {[regexp {[a-z]+} $value] == 1} {
    puts "Val: $value"
    set value $notes($value)
    puts "Val set to $value"
    #clarify this.
  }
  puts "For: $target Notes: $notes($target) Value: $value on level $x"
  switch $cmd {
    snd {
      puts "send $value to $notes($note) from $note"
      set notes($note) $value
    }
    set {
      puts "set $target to $value"
      set notes($target) $value
    }
    add {
      puts "add notes($target) to $value"
      set notes($target) [expr {$notes($target) + $value}]
    }
    mul {
      puts "multiplied $value by $notes($target)"
      set notes($target) [expr {$notes($target) * $value}]
    }
    mod {
      puts "mod set notes($target) to [expr {$notes($target) % $value}]"
      set notes($target) [expr {$notes($target) % $value}]
    }
    rcv {
      if {$notes($note) != 0} {
      puts "rcv notes($target) to $notes($note) from $note"
        set notes($target) $notes($note)
      }
    }
    jgz {
      if {$notes($target) > 0} {
        incr x $value
      }
    }
  }
}
