package main

import (
	"flag"
	"log"
	"strconv"
)

// Node blah blah
type Node struct {
	val  int
	next *Node
}

// NewNode blah blah
func NewNode(val int, next *Node) *Node {
	return &Node{val: val, next: next}
}

func both(steps, vals int, after bool) int {
	curval := 0
	head := NewNode(curval, nil)
	head.next = head
	curnode := head

	for v := 0; v < vals; v++ {
		for i := 0; i < steps; i++ {
			curnode = curnode.next
		}
		curval++
		node := NewNode(curval, curnode.next)
		curnode.next = node
		curnode = node
	}

	if after {
		curnode = head
		for curnode.val != 0 {
			curnode = curnode.next
		}
	}

	return curnode.next.val
}

func main() {
	flag.Parse()
	if flag.NArg() == 0 {
		log.Fatal("missing input")
	}

	if steps, err := strconv.Atoi(flag.Arg(0)); err == nil {
		log.Printf("one %d", both(steps, 2017, false))
		log.Printf("two %d", both(steps, 50000000, true))
	} else {
		log.Fatal(err)
	}
}
