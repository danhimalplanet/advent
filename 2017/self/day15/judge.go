package main

import (
	"log"
	"sync"
)

var wg sync.WaitGroup

func generator(start, factor, multfactor int, outchan chan<- int) {
	var cur = start
	for {
		cur = cur * factor % 2147483647
		if cur % multfactor == 0 {
			outchan <- cur
		}
	}
}

func judge(chan1, chan2 <-chan int, limit int, part string) {
	var in1, in2, matches int

	for i := 0; i < limit; i++ {
		in1 = <- chan1
		in2 = <- chan2
		in1 = in1 & 65535
		in2 = in2 & 65535
		if in1 == in2 {
			// log.Printf("%s found at %d: %d", part, i, matches+1)
			matches++
		}
	}
	log.Printf("%s done: %d", part, matches)
	wg.Done()
}


func main() {
	log.Println("starting")

	// part 1
	var chan1 = make(chan int)
	var chan2 = make(chan int)

	go generator(722, 16807, 1, chan1)
	go generator(354, 48271, 1, chan2)
	wg.Add(1)
	go judge(chan1, chan2, 40000000, "part1")

	// part 2
	var chan3 = make(chan int)
	var chan4 = make(chan int)

	go generator(722, 16807, 4, chan3)
	go generator(354, 48271, 8, chan4)
	wg.Add(1)
	go judge(chan3, chan4, 5000000, "part2")

	wg.Wait()
}
