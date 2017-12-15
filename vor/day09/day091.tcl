set fsize [file size "day09.txt"]
set fp [open "day09.txt" r]
set stream [read $fp $fsize]
close $fp

regsub -all {!!|!>} $stream {} swap
regsub -all {<(?:[^>]+)?>|,} $swap {} swap
puts $swap

for {set x 1}{$x != $x} {incr x} {
# if ({([\d,]+)})
#   find all (?<={)([\d,]+)(?=}) and increase each number by 1
#   find all ({([\d,]+)}) and replace with 1,$2
# else break
}
# sum all ,
# puts $total