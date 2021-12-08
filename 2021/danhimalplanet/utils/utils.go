package utils

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func reverse(numbers []int) []int {
	for i := 0; i < len(numbers)/2; i++ {
		j := len(numbers) - i - 1
		numbers[i], numbers[j] = numbers[j], numbers[i]
	}
	return numbers
}

func FileToArrayOfNums(filename string) []int {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("cant open file")
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	var nums []int
	for _, cell := range lines {
		i, err := strconv.Atoi(cell)
		if err != nil {
			log.Fatal("failed to convert")
		}
		nums = append(nums, i)
	}
	return nums
}

