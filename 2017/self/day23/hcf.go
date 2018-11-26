package main

import (
	"bufio"
	"flag"
	"log"
	"os"
	"strconv"
	"strings"
)

func val(regs map[string]int, thing string) int {
	var v int
	var ok bool

	if v, ok = regs[thing]; !ok {
		v, _ = strconv.Atoi(thing)
	}
	return v
}

func one(instructions []string) {
	jumpout := len(instructions)
	var regs = make(map[string]int)

	var parts []string
	var pc, mulcount, jmp int

	for {
		if pc < 0 || pc >= jumpout {
			log.Printf("muls: %d", mulcount)
			return
		}
		parts = strings.Split(instructions[pc], " ")
		switch parts[0] {
		case "set":
			regs[parts[1]] = val(regs, parts[2])
			pc++
		case "sub":
			regs[parts[1]] -= val(regs, parts[2])
			pc++
		case "mul":
			regs[parts[1]] *= val(regs, parts[2])
			mulcount++
			pc++
		case "jnz":
			check := val(regs, parts[1])
			if check != 0 {
				jmp = val(regs, parts[2])
				pc += jmp
			} else {
				pc++
			}
		default:
			panic(parts[0])
		}
	}

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

	var instructions []string

	scanner := bufio.NewScanner(infile)
	for scanner.Scan() {
		instructions = append(instructions, scanner.Text())
	}

	log.SetOutput(os.Stdout)

	one(instructions)
}
