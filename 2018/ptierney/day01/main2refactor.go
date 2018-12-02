package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func getInput() []string {
	file, err := os.Open("input")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	var inputList []string

	for scanner.Scan() {
		inputList = append(inputList, scanner.Text())
	}

	return inputList
}

func getInputInt() []int {
	inputStrings := getInput()

	inputInts := make([]int, len(inputStrings))

	for i, v := range inputStrings {
		convertedInt, err := strconv.Atoi(v)

		if err != nil {
			log.Fatal(err)
		}

		inputInts[i] = convertedInt
	}

	return inputInts
}

func containsTwo(s string) bool {

}

func containsThree(s string) bool {

}

func main() {
	inputFrequencies := getInputInt()
	frequencies := make(map[int]bool)
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
