package main

import (
	"bufio"
	"flag"
	"log"
	"os"
	"strconv"
	"strings"
)

// Program blah blah
type Program []string

func (p Program) String() string {
	return strings.Join(p, "")
}

func dance(moves []string, programs Program) Program {
	for _, move := range moves {
		switch string(move[0]) {
		case "s":
			amount, _ := strconv.Atoi(move[1:])
			var left, right Program
			left, right = programs[len(programs)-amount:], programs[0:len(programs)-amount]
			programs = append(left, right...)
		case "x":
			parts := strings.Split(move[1:], "/")
			a, _ := strconv.Atoi(parts[0])
			b, _ := strconv.Atoi(parts[1])
			programs[a], programs[b] = programs[b], programs[a]
		case "p":
			a := string(move[1])
			b := string(move[3])
			var ia, ib int
			for i := 0; i < len(programs); i++ {
				if programs[i] == a {
					ia = i
				} else if programs[i] == b {
					ib = i
				}
			}
			programs[ia], programs[ib] = programs[ib], programs[ia]
		}
	}

	return programs
}

func one(moves Program, programs Program) Program {
	return dance(moves, programs)
}

// the only way to compare slices
func isSame(program1, program2 Program) bool {
	for i := 0; i < len(program1); i++ {
		if program1[i] != program2[i] {
			return false
		}
	}

	return true
}

// this code is not a code of honor.
func two(moves Program, programs Program) Program {
	var start = make(Program, len(programs))
	var first = make(Program, len(programs))
	var cycle int

	// we'll need it later
	copy(start, programs)

	programs = dance(moves, programs)
	// we'll need to compare against to find the cycle
	copy(first, programs)
	i := 1
	for {
		programs = dance(moves, programs)
		i++

		if isSame(programs, first) {
			cycle = i + 1
			break
		}
	}

	mod := 1000000001 % cycle
	log.Printf("cycle %d mod %d", cycle, mod)

	// return to starting position, and run the loop mod+1 times
	copy(programs, start)
	for i = 0; i <= mod; i++ {
		programs = dance(moves, programs)
	}

	return programs
}

func main() {
	var err error

	flag.Parse()
	if flag.NArg() == 0 {
		log.Fatal("missing input filename")
	}

	infile, err := os.Open(flag.Arg(0))
	if err != nil {
		log.Fatal(err)
	}

	defer infile.Close()

	var moves []string

	scanner := bufio.NewScanner(infile)
	if scanner.Scan() {
		moves = strings.Split(scanner.Text(), ",")
	} else {
		log.Fatal(scanner.Err())
	}

	var original = Program{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"}
	var programs = make(Program, len(original))

	copy(programs, original)
	log.Println(one(moves, programs))

	// reset before the second part
	copy(programs, original)
	log.Println(two(moves, programs))
}
