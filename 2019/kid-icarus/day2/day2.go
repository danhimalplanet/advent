package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func add(nums []int, a int, b int, output int) []int {
	nums[output] = nums[a] + nums[b]
	return nums
}

func multiply(nums []int, a int, b int, output int) []int {
	nums[output] = nums[a] * nums[b]
	return nums
}

func compute (input []int, noun int, verb int) int{
	nums := input[:]
	nums[1] = noun
	nums[2] = verb
	for i := 0; i < len(nums) -4; i += 4 {
		if nums[i] == 99 {
			break
		}
		if nums[i] == 1 {
			nums = add(nums, nums[i + 1], nums[i + 2], nums[i + 3])

		} else if nums[i] == 2 {
			nums = multiply(nums, nums[i + 1], nums[i + 2], nums[i + 3])
		}
	}
	return nums[0]
}

func makeNums(numStrs []string) []int {
	nums := make([]int, len(numStrs))
	for i, num := range numStrs {
		numInt, _ := strconv.Atoi(num)
		nums[i] = numInt
	}
	return nums
}

func main() {
	pwd, _ := os.Getwd()
	dat, err := ioutil.ReadFile(pwd + "/part1.txt")
	numStrs := strings.Split(string(dat), ",")
	if err != nil {
		fmt.Println("err")
	}

	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			if compute(makeNums(numStrs), noun, verb) == 19690720 {
				fmt.Println(100 * noun + verb)
			}
		}
	}
}
