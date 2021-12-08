package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type command struct {
	direction string
	magnitude int
}

func main() {
	args := os.Args
	filename := ""
	if len(args) != 2 {
		filename = "example.txt"
	} else {
		filename = args[1]
	}

	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("cant open file")
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var commands []command
	for scanner.Scan() {
		s := strings.Split(scanner.Text(), " ")
		direction := s[0]
		magnitude, _ := strconv.Atoi(s[1])
		commands = append(commands, command{direction: direction, magnitude: magnitude})
	}

	position := 0
	depth := 0

	for _, command := range commands {
		switch command.direction {
		case "forward":
			position += command.magnitude
		case "down":
			depth += command.magnitude
		case "up":
			depth -= command.magnitude
		}
	}

	fmt.Println("Part 1:")
	fmt.Println("position:", position)
	fmt.Println("depth:", depth)
	fmt.Println("position * depth =", position*depth)

	aim := 0
	position = 0
	depth = 0

	for _, command := range commands {
		switch command.direction {
		case "forward":
			position += command.magnitude
			depth += aim * command.magnitude
		case "down":
			aim += command.magnitude
		case "up":
			aim -= command.magnitude
		}
	}

	fmt.Println("Part 2:")
	fmt.Println("position:", position)
	fmt.Println("depth:", depth)
	fmt.Println("position * depth =", position*depth)

}
