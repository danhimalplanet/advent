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

	frequencies := make(map[int]bool)

	var inputFrequencies []int

	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())

		if err != nil {
			log.Fatal(err)
		}

		inputFrequencies = append(inputFrequencies, i)
	}

	sum := 0

	for {
		for _, v := range inputFrequencies {

			sum += v

			// Check if the sum is in the map
			if _, success := frequencies[sum]; success {
				fmt.Printf("First repeat: %v\n", sum)
				return
			}

			frequencies[sum] = true
		}
	}
}
