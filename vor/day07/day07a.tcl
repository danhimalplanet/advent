set fsize [file size "day07.txt"]
set fp [open "day07.txt" r]
set tower [read $fp $fsize]
close $fp

set layer [split $tower '\n']
set branch [lsearch -all $layer *\-\>*]
foreach i $branch {
  set forker [string trim [lindex [split [lindex $layer $i] '('] 0]]  
  set matcher [lsearch -all $layer *$forker*]
  if ([expr {[llength $matcher]} < 2]) {
    puts $forker
  }
}
