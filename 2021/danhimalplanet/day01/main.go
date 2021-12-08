package main

import (
	"kvas.tech/gitea/advent/utils"
	"fmt"
	"os"
)

func main() {
	args := os.Args
	filename := ""
	if len(args) != 2 {
		filename = "example.txt"
	} else {
		filename = args[1]
	}
	nums := utils.FileToArrayOfNums(filename)

	counter := 0

	for i := 0; i < len(nums); i++ {
		if i > 0 {
			if nums[i] > nums[i-1] {
				fmt.Println(nums[i], "increased")
				counter += 1
			} else if nums[i] < nums[i-1] {
				fmt.Println(nums[i], "decreased")
			} else {
				fmt.Println(nums[i], "no change")
			}
		}
	}
	fmt.Println("Part 1 Result:", counter)

	counter = 0
	for i := 1; i <= len(nums); i++ {
		if len(nums)-i > 2 {
			previous_sum := nums[i-1] + nums[i] + nums[i+1]
			current_sum := nums[i] + nums[i+1] + nums[i+2]
			if current_sum > previous_sum {
				fmt.Println(current_sum, "increased")
				counter += 1
			} else if current_sum < previous_sum {
				fmt.Println(current_sum, "decreased")
			} else {
				fmt.Println(current_sum, "no change")
			}
		}
	}
	fmt.Println("Part 2 Result:", counter)
}
