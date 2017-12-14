set fsize [file size "day11.txt"]
set fp [open "day11.txt" r]
set instructions [read $fp $fsize]
close $fp
set instructions [expr {[split $instructions ',']}]

foreach j $instructions {
#f(x,y) (((x1 + y1)+(x2 + y2)) - 1)
# steps = x's and y's minus 1.  use abs, as to not mess up the math with negs.

#N  = y - 1
#N@ = y + 0
#S  = y + 1

# E = x + 1
# 	= x + 0
# W = x - 1

	puts $j
}
