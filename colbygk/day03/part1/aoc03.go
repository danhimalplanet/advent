package main

import "fmt"

// Based on Ulam's Spiral
//   There is a recurrence relation that
//     defines the size of each successfu layer
//     in the spiral
//     a_n = (8*n) + a_(n-1)
//   Then, using modular arithmetic, solve for
//     the position of the number within the given
//     layer
func computeDistance(t int) int {
	a := 0
	b := 1
	c := 0

	// The recurrence relation
	for b < t {
		c = b
		b = (a * 8) + c
		a = a + 1
	}

	// Modular arithmetic to determine the final
	// distance
	// e.g.
	// If given number is within the spiral with 23
	// numbers, e.g. 26 - 49, then modulo for one side
	// is:
	// 1       2       3       4       5       0       1
	// 6       5       4       3       4       5       6
	// n      n-1     n-2     n-3     n-2     n-1      n

	n := ((b - (c + 1)) / 4) + 1
	m := t % n

	if m == 0 {
		return (n - 1)
	}
	k := 0
	pivot := (n / 2) + 1
	for i := 1; i < n; i++ {
		if i == m {
			return (n + k)
		}
		if i < pivot {
			k = k - 1
		} else {
			k = k + 1
		}
	}
	return 0
}

var answer int

func main() {
	tests := [][]int{{1, 0}, {12, 3}, {23, 2}, {1024, 31}}

	for _, e := range tests {
		answer = computeDistance(e[0])
		fmt.Printf("Test %v, %v == %v, %v\n",
			e[0], e[1], answer, answer == e[1])
	}

	fmt.Printf("Part1: %v, answer: %v\n",
		347991, computeDistance(347991))
}
