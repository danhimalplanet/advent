set fsize [file size "day08.txt"]
set fp [open "day08.txt" r]
set instruct [read $fp $fsize]
close $fp

set steps [split $instruct '\n']
set step [lindex $steps 0]
puts "step\: $step"
set iffer [string trim [expr {[lindex [split $step 'if'] 2]}]]
puts "iffer\: $iffer"
set names [split $iffer " "]
puts "names\: $names"