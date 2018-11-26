set fsize [file size "day08.txt"]
set fp [open "day08.txt" r]
set instruct [read $fp $fsize]
close $fp

array set pocket {}

set largest 0
foreach step [split $instruct '\n'] {
  set instruction   [split [string trim [expr {[lindex [split [expr {[string map {{ if } {:}} $step]}] ':'] 0]}]] " "]
  set ins_name      [expr {[lindex $instruction 0]}]
  set ins_direction [expr {[lindex $instruction 1]}]
  set ins_duration  [expr {[lindex $instruction 2]}]
  
  set condition     [split [string trim [expr {[lindex [split [expr {[string map {{ if } {:}} $step]}] ':'] 1]}]] " "]
  set con_name      [expr {[lindex $condition 0]}]
  set con_value [expr {[info exists pocket($con_name)]? $pocket($con_name) : 0 } ]
  set con_symbol    [expr {[lindex $condition 1]}]
  set con_result    [expr {[lindex $condition 2]}]

  if {[expr ($con_value $con_symbol $con_result)]} {
    set ins_value [expr {[info exists pocket($ins_name)]? $pocket($ins_name) : 0 } ]
    set pocket($ins_name) [expr {$ins_value + [expr {($ins_direction eq "inc")? $ins_duration : -$ins_duration }]}]
    set largest [expr {$pocket($ins_name) > $largest ? $pocket($ins_name) : $largest}]
  }
}
puts $largest
