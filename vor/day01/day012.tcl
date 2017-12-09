set fsize [file size "day01.txt"]
set fp [open "day01.txt" r]
set secret [read $fp $fsize]
close $fp

set len_secret [string length $secret]
set sumtotal 0
set jump [expr {$len_secret / 2}]

for {set m 0} {$m < $len_secret} {incr m} {
    set start [string index $secret $m]
    
    if {$m + $jump >= $len_secret} { 
        set offset [expr {$jump + $m - $len_secret}]
    } else {
        set offset [expr {$jump + $m}]
    }
    set comparer [string index $secret $offset]
    if {$start == $comparer} {
        set sumtotal [expr {$sumtotal + $start}]
    }
}
puts "$sumtotal"
