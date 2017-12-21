set input 289326
set layer 0
set total 0
array set grid {} 
set x 5
set y 5
set thisxy [expr {($x * 10) + $y}]
set direction right

# MOVE

    #right: 10s increase 1s same

    #up: x same y increase

    #left: x decrease y same

    #down: x same y decrease


# CALCULATE

 
            # right
            set tindex [expr {(($x + 1) * 10) + $y}]
            puts $tindex 
            set grid($tindex) 24  
            #need to check for array, and remove that 24 above
            puts [expr {$grid($tindex) == "" ? 0 : $grid($tindex)}]
      
            # top right
            set tindex [expr {(($x + 1) * 10) + ($y + 1)}] 
            # top
            set tindex [expr {($x * 10) + ($y + 1)}]
            # top left
            set tindex [expr {(($x - 1) * 10) + ($y + 1)}] 
            # left
            set tindex [expr {(($x - 1) * 10) + $y}] 
            # bottom left
            set tindex [expr {(($x - 1) * 10) + ($y - 1)}] 
            # bottom
            set tindex [expr {($x * 10) + ($y - 1)}]
            # bottom right
            set tindex [expr {(($x + 1) * 10) + ($y - 1)}] 
    #puts $tindex
    #set total [expr {$total + {[lindex $grid $tindex] != "" ? [lindex $grid $tindex] : 0}}]

#lset grid $thisxy $total
#}

