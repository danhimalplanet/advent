package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func add(nums []int, i int, mode string ) []int {
	var a int
	var b int
	if mode[len(mode) - 1:] == "0" {
		a = nums[nums[i + 1]]
	} else {
		a = nums[i + 1]
	}
	if mode[0:1] == "0" {
		b = nums[nums[i + 2]]
	} else {
		b = nums[i + 2]
	}
	nums[nums[i + 3]] = a + b
	return nums
}

func multiply(nums []int, i int, mode string ) []int {
	var a int
	var b int
	if mode[len(mode) - 1:] == "0" {
		a = nums[nums[i + 1]]
	} else {
		a = nums[i + 1]
	}
	if mode[0:1] == "0" {
		b = nums[nums[i + 2]]
	} else {
		b = nums[i + 2]
	}
	nums[nums[i + 3]] = a * b
	return nums
}

func jump(nums []int, i int, mode string, isNonZero bool ) int {
	var a int
	var b int
	if mode[len(mode) - 1:] == "0" {
		a = nums[nums[i + 1]]
	} else {
		a = nums[i + 1]
	}
	if mode[0:1] == "0" {
		b = nums[nums[i + 2]]
	} else {
		b = nums[i + 2]
	}
	if isNonZero && a != 0 {
		return b
	}
	if !isNonZero && a == 0 {
		return b
	}
	return i + 3
}

func compare(nums []int, i int, mode string, comparator string) []int {
	var a int
	var b int
	address := nums[i + 3]
	if mode[len(mode) - 1:] == "0" {
		a = nums[nums[i + 1]]
	} else {
		a = nums[i + 1]
	}
	if mode[0:1] == "0" {
		b = nums[nums[i + 2]]
	} else {
		b = nums[i + 2]
	}
	if comparator == "lt" {
		if a < b {
			nums[address] = 1
		} else {
			nums[address] = 0
		}
	} else if comparator == "eq"{
		if a == b {
			nums[address] = 1
		} else {
			nums[address] = 0
		}
	}
	return nums
}

const (
	ad = "01"
	mul = "02"
	mov = "03"
	out = "04"
	jmpt = "05"
	jmpf = "06"
	lt = "07"
	eq = "08"
	halt = "99"
)

func LeftPad2Len(s string, padStr string, overallLen int) string {
	var padCountInt = 1 + ((overallLen - len(padStr)) / len(padStr))
	var retStr = strings.Repeat(padStr, padCountInt) + s
	return retStr[(len(retStr) - overallLen):]
}

func compute (instructions []int, input int) []int {
	nums := instructions[:]
	i := 0
	for {
		instruction := strconv.Itoa(nums[i])
		var mode string
		var opCode string
		if len(instruction) == 1 {
			opCode = LeftPad2Len(instruction, "0", 2)
		} else {
			opCode = instruction[len(instruction) - 2:]
		}

		switch opCode {
		case halt:
			return nums
		case mov:
			nums[nums[i + 1]] = input
			i+=2
		case out:
			if len(instruction) > 2 {
				mode = instruction[:len(instruction) - 2]
			} else {
				mode = "0"
			}
			if mode == "1" {
				fmt.Println(nums[i + 1])
			} else {
				fmt.Println(nums[nums[i + 1]])
			}
			i += 2
		case mul:
			if len(instruction) > 2 {
				mode = LeftPad2Len(instruction[:len(instruction) - 2], "0", 2)
			} else {
				mode = "00"
			}
			nums = multiply(nums, i, mode)
			i += 4
		case ad:
			if len(instruction) > 2 {
				mode = LeftPad2Len(instruction[:len(instruction) - 2], "0", 2)
			} else {
				mode = "00"
			}
			nums = add(nums, i, mode)
			i += 4
		case jmpt:
			if len(instruction) > 2 {
				mode = LeftPad2Len(instruction[:len(instruction) - 2], "0", 2)
			} else {
				mode = "00"
			}
			i = jump(nums, i, mode, true)
		case jmpf:
			if len(instruction) > 2 {
				mode = LeftPad2Len(instruction[:len(instruction) - 2], "0", 2)
			} else {
				mode = "00"
			}
			i = jump(nums, i, mode, false)
		case lt:
			if len(instruction) > 2 {
				mode = LeftPad2Len(instruction[:len(instruction) - 2], "0", 2)
			} else {
				mode = "00"
			}
			nums = compare(nums, i, mode, "lt")
			i += 4
		case eq:
			if len(instruction) > 2 {
				mode = LeftPad2Len(instruction[:len(instruction) - 2], "0", 2)
			} else {
				mode = "00"
			}
			nums = compare(nums, i, mode, "eq")
			i += 4
		}

	}
	return nums
}

func main() {
	pwd, _ := os.Getwd()
	raw, err := ioutil.ReadFile(pwd + "/input.txt")
	if err != nil {
		panic(err)
	}
	input := string(raw)
	instructionStr := strings.Split(strings.Trim(input, " \n"), ",")
	var nums []int
	for _, str := range instructionStr {
		num, _ := strconv.Atoi(str)
		nums = append(nums, num)
	}
	compute(nums, 5)
}
