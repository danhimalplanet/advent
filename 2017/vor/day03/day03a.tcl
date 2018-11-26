set input 289326
set runner [expr {round(sqrt($input))}]
set lower [expr {($runner * ($runner - 1)) + 1}]
set higher [expr {$runner * ($runner + 1)}]
set ldiff [expr {$input - $lower}]
set hdiff [expr {$higher - $input}]

puts "for $input the runner is $runner and lower is $lower and higher is $higher and ldiff is $ldiff and hdiff is $hdiff"

if ([expr {$runner % 2 == 0}]) {        
    if ([expr {$input <= ($higher - $runner)}]) {
        set x [expr {$runner / 2}]
        set y [expr {($runner / 2) - $ldiff}]
        puts "x is $x and y is $y to equal [expr {abs($x) + abs($y)}]"

    } else {
        set x [expr {(0 - ($runner / 2} - 1)) + $hdiff]
        set y [expr {0 - ($runner / 2)}]
        puts "x is $x and y is $y to equal [expr {abs($x) + abs($y)}]"
    }
} else {
    if ([expr {$input <= ($higher - $runner)}]) {       
        set x [expr {0 - ($runner - 1 ) / 2}]
        set y [expr {(0 - ($runner / 2)) + $ldiff}]
        puts "x is $x and y is $y to equal [expr {abs($x) + abs($y)}]"
    } else {
        set y [expr {(($runner - 1 ) / 2) + 1}]
        set x [expr {(($runner - 1 ) / 2) - $hdiff}]
        puts "4. x is $x and y is $y to equal [expr {abs($x) + abs($y)}]"
    }
}
