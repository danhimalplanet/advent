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

func differsByOne(s1 string, s2 string) bool {
	numDifferent := 0

	for i, _ := range s1 {
		if s1[i] != s2[i] {
			numDifferent += 1
		}

		if numDifferent > 1 {
			return false
		}
	}

	return numDifferent == 1
}

func main() {
	inputIDs := getInput()

	for i := 0; i < len(inputIDs); i++ {
		for j := i + 1; j < len(inputIDs); j++ {
			if differsByOne(inputIDs[i], inputIDs[j]) {
				fmt.Printf("Box 1: %v\nBox 2: %v\n", inputIDs[i], inputIDs[j])
				return
			}
		}
	}
}
