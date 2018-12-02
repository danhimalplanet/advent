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

func containsN(s string, n int) bool {
	letterMap := make(map[rune]int)

	for _, char := range s {
		letterMap[char] = letterMap[char] + 1
	}

	for _, value := range letterMap {
		if value == n {
			return true
		}
	}

	return false
}

func containsTwo(s string) bool {
	return containsN(s, 2)
}

func containsThree(s string) bool {
	return containsN(s, 3)
}

func main() {
	inputIDs := getInput()

	containsTwoCount := 0
	containsThreeCount := 0

	for _, id := range inputIDs {
		if containsTwo(id) {
			containsTwoCount += 1
		}

		if containsThree(id) {
			containsThreeCount += 1
		}
	}

	checksum := containsTwoCount * containsThreeCount

	fmt.Printf("Checksum: %v\n", checksum)
}
