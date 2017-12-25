package main

import (
	"log"
)

type position int
type value int

const (
	done  = 12794428
	left  = -1
	right = 1
	a     = iota
	b
	c
	d
	e
	f
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
				state = f
			}
		case b:
			switch val {
			case 0:
				tape[pos] = 0
				pos += right
				state = c
			case 1:
				tape[pos] = 0
				pos += right
				state = d
			}
		case c:
			switch val {
			case 0:
				tape[pos] = 1
				pos += left
				state = d
			case 1:
				tape[pos] = 1
				pos += right
				state = e
			}
		case d:
			switch val {
			case 0:
				tape[pos] = 0
				pos += left
				state = e
			case 1:
				tape[pos] = 0
				pos += left
				state = d
			}
		case e:
			switch val {
			case 0:
				tape[pos] = 0
				pos += right
				state = a
			case 1:
				tape[pos] = 1
				pos += right
				state = c
			}
		case f:
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
