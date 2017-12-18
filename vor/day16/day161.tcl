set fsize [file size "day16.txt"]
set fp [open "day16.txt" r]
set instructions [read $fp $fsize]
close $fp

set instructions [split $instructions ","]
set stage {a b c d e f g h i j k l m n o p}

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

puts $stage
