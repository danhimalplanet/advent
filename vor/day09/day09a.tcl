set fsize [file size "day09.txt"]
set fp [open "day09.txt" r]
set stream [read $fp $fsize]
close $fp

set layer 1
regsub -all {!!|!>} $stream {} swap
regsub -all {<(?:[^>]+)?>|,} $swap {} swap
puts $swap

regsub -all {\{\}} $swap {1,} swap
puts $swap

while 1 {

# if ({([\d,]+)})
#   find all (?<={)([\d,]+)(?=}) and increase each number by 1
#   find all ({([\d,]+)}) and replace with 1,$2
# else break
	break
}

# sum all ,
# puts $total