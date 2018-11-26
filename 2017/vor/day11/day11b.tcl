set fsize [file size "day11.txt"]
set fp [open "day11.txt" r]
set instructions [read $fp $fsize]
close $fp

set instructions [expr {[split $instructions ',']}]
set x 0
set y 0
set maxdist 0
foreach j $instructions {
  if {[string length $j] == 1} {
    set y [expr {$j == "n"? $y - 1: $y + 1}]
  } else {
    if {[string range $j 0 0] == "n" && $x % 2 != 0} {
      set y [expr {$y - 1}]      
    } 
    
    if {[string range $j 0 0] == "s" && $x % 2 == 0} {
      set y [expr {$y + 1}]   
    } 
    set x [expr {[string range $j 1 1] == "e"? $x + 1: $x - 1}]
  }
  
  set ax [expr { abs($x) }]
  set ay [expr { abs($y) }]
  if {$ax > $ay} {
    if {$ay < round($ax/2)} {
      set z $ax
    } else {
    set z [expr {$ax/2 + $ay}]
    }
  } elseif {$ay > $ax} {
    set z [expr {($ay - $ax/2) + $ax}]
  } else {
    set z [expr {$ax * 1.5}]
  }
  if {$z > $maxdist} {
    set maxdist $z
  }
}
puts $maxdist
