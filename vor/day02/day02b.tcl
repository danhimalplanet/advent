set fsize [file size "day02.txt"]
set fp [open "day02.txt" r]
set spread [read $fp $fsize]
close $fp

set checksum 0

foreach i [split $spread '\n'] {
    set sorts [lsort -integer $i]
    foreach j $sorts {
        foreach k $sorts {
            if {$j != $k} {
                if {[expr {fmod($k,$j)} == 0] == 1} {
                    set checksum [expr {$checksum + [expr {$k / $j}]}]
                }
            }
        }
    }
}
puts $checksum

