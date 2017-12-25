set limit 12425180
set current $limit
set state A
set cycle {}

array set tape {}
set tape($current) 0

for {set x 0} {$x < $limit} {incr x} {
  set checkstate $state
  switch $checkstate {
    A {
        if {$tape($current) == 0} {
          set tape($current) 1
          set current [expr {$current + 1}]
          set state B
        } else {
          set tape($current) 0
          set current [expr {$current + 1}]
          set state F
        }
      }
    B {
        if {$tape($current) == 0} {
          set tape($current) 0
          set current [expr {$current - 1}]
          set state B
        } else {
          set tape($current) 1
          set current [expr {$current - 1}]
          set state C
        }
      }
    C {
        if {$tape($current) == 0} {
          set tape($current) 1
          set current [expr {$current - 1}]
          set state D
        } else {
          set tape($current) 0
          set current [expr {$current + 1}]
          set state C
        }
      }
    D {
        if {$tape($current) == 0} {
          set tape($current) 1
          set current [expr {$current - 1}]
          set state E
        } else {
          set tape($current) 1
          set current [expr {$current + 1}]
          set state A
        }
      }
    E {
        if {$tape($current) == 0} {
          set tape($current) 1
          set current [expr {$current - 1}]
          set state F
        } else {
          set tape($current) 0
          set current [expr {$current - 1}]
          set state D
        }
      }    
    F {
        if {$tape($current) == 0} {
          set tape($current) 1
          set current [expr {$current + 1}]
          set state A
        } else {
          set tape($current) 0
          set current [expr {$current - 1}]
          set state E
        }
      }
  }
  if {[info exists tape($current)] == 0} {
    set tape($current) 0
  }
}
puts [regexp -all {\s1\s} [array get tape]]

