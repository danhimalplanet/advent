package main

import "log"

type position int
type value int

const (
	done  = 6
	left  = -1
	right = 1
	a     = iota
	b
)

func startmachine() {
	var tape = make(map[position]value)
	state := a
	var pos position
	var val, ones value

	for steps := 0; steps < done; steps++ {
		val = tape[pos]
		switch state {
		case a:
			switch val {
			case 0:
				tape[pos] = 1
				pos += right
				state = b
			case 1:
				tape[pos] = 0
				pos += left
				state = b
			}
		case b:
			switch val {
			case 0:
				tape[pos] = 1
				pos += left
				state = a
			case 1:
				tape[pos] = 1
				pos += right
				state = a
			}
		}
	}

	for _, val = range tape {
		if val == 1 {
			ones++
		}
	}
	log.Println(ones)
}

func main() {
	startmachine()
}

// eof
