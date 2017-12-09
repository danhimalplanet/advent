set memory "10  3 15  10  5 15  5 15  9 2 5 8 5 2 3 6"

set banks 16

set savestate ""
set swaplist ""
lset swaplist 0 $memory
lset savestate 0 $swaplist


for {set x 1} {$x == $x} {incr x} {
    set tmax [::tcl::mathfunc::max {*}[lmap v $memory {expr {$v}}]]
    set tmaxindex [lsearch $memory $tmax]
    set tbottom [format "%.0f" [expr {floor($tmax / $banks)}]]
    set tdiff [expr {$tmax - ($banks * $tbottom)}]

    lset memory $tmaxindex 0

    set blockstep [expr $tmaxindex == ($banks - 1) ? 0: {$tmaxindex + 1}]
    for {set y 1} {$y <= $tdiff} {incr y} {
        lset memory $blockstep [expr {[lindex $memory $blockstep] + $tbottom + 1}]
        set blockstep [expr $blockstep == ($banks - 1) ? 0: $blockstep + 1]
    }
    for {set y 1} {$y <= ($banks - $tdiff)} {incr y} {
        lset memory $blockstep [expr {[lindex $memory $blockstep] + $tbottom}]
        set blockstep [expr $blockstep == ($banks - 1) ? 0: $blockstep + 1]
    }

    lset swaplist 0 $memory
    
    set used [lsearch $savestate $swaplist]
    if {$used != -1} {
        puts [expr {$x - $used}]
        break
    }
    lset savestate $x $swaplist
}