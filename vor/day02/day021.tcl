set fsize [file size "day02.txt"]
set fp [open "day02.txt" r]
set spread [read $fp $fsize]
close $fp

set checksum 0
foreach i [split $spread '\n'] {
set tnums [split $i " "]
set tmin [::tcl::mathfunc::min {*}[lmap v $tnums {expr {$v}}]]
set tmax [::tcl::mathfunc::max {*}[lmap v $tnums {expr {$v}}]]
set checksum [expr {$checksum + [expr {$tmax - $tmin}]}]
}
puts $checksum
