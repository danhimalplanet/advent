package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	sum := 0

	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())

		if err != nil {
			log.Fatal(err)
		}

		sum += i
	}

	fmt.Printf("Sum: %v\n", sum)
}
