set fsize [file size "day04.txt"]
set fp [open "day04.txt" r]
set spread [read $fp $fsize]
close $fp

set checksum 0
foreach i [split $spread '\n'] {
    set bad 0
    set jindex 0
    foreach j $i {
        incr jindex
        set kindex 0
        foreach k $i {
            incr kindex
            if {($bad == 0 && $jindex != $kindex) && ($k eq $j || [lsort [split $j {}]] == [lsort [split $k {}]])} {
                set bad 1
            }
        }
    }
    if {$bad == 0} {
        incr checksum
    }
}
puts $checksum
