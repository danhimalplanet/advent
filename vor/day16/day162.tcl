set fsize [file size "day16.txt"]
set fp [open "day16.txt" r]
set instructions [read $fp $fsize]
close $fp

set instructions [split $instructions ","]
set stage {a b c d e f g h i j k l m n o p}
set storage {}
set cycle 0
set cycleplus 1000000000
set cyclemaker false

for {set z 0} {$z < $cycleplus} {incr z} {
  foreach i $instructions {
    switch [string index $i 0] {
        s {
          set spin [string range $i 1 10]
          set offset [expr {16 - $spin}]
          set swap {}
          for {set x 0} {$x < $spin} {incr x} {
            lset swap $x [lindex $stage  [expr {$x + $offset}]]
          }
          set stage [concat $swap [lrange $stage 0 [expr {$offset - 1}]]]
        }
        x {
          set exchange [split [string range $i 1 10] "/"]
          set first [lindex $stage [lindex $exchange 0]]
          set last [lindex $stage [lindex $exchange 1]]
          lset stage [lindex $exchange 0] $last
          lset stage [lindex $exchange 1] $first
        }
        p {
          set partner [split [string range $i 1 10] "/"]
          set indexfirst [lsearch $stage [lindex $partner 0]]
          set indexlast [lsearch $stage [lindex $partner 1]]
          set first [lindex $stage $indexfirst]
          set last [lindex $stage $indexlast]
          lset stage $indexfirst $last
          lset stage $indexlast $first       
        }
    }  
  }
 
  if {[lsearch $storage $stage] == -1 && $cyclemaker == true} { 
    lappend storage $stage
  } else {
    set cycle $z
    set cycleplus [expr {$cycle + [expr {1000000000 % 60}]}]
    set cyclemaker true
  }
}
puts [join $stage ""]
