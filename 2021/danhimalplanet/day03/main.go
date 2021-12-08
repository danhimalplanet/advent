package main

import (
	"bufio"
	_ "encoding/binary"
	"fmt"
	"log"
	"os"
	"strconv"
)

func GenericFilter(reports [][]int, position int, target int) [][]int {
	var d [][]int
	for _, report := range reports {
		if report[position] == target {
			d = append(d, report)
		}
	}
	return d
}

func MemberCount(reports [][]int, position int, target int) int {
	zeros := 0
	ones := 0
	for _, report := range reports {
		if report[position] == 1 {
			ones += 1
		} else {
			zeros += 1
		}
	}
	if target == 1 {
		return ones
	} else {
		return zeros
	}
}

func CountNumColumn(reports [][]int, position int, value int) int {
	count := 0
	for _, report := range reports {
		if report[position] == value {
			count += 1
		}
	}
	return count
}

func MostCommonInColumn(reports [][]int, position int) int {
	zeros := 0
	ones := 0
	for _, report := range reports {
		if report[position] == 0 {
			zeros += 1
		}
		if report[position] == 1 {
			ones += 1
		}
	}
	if zeros > ones {
		return 0
	} else {
		return 1
	}
}

func LeastCommonInColumn(reports [][]int, position int) int {
	zeros := 0
	ones := 0
	for _, report := range reports {
		if report[position] == 0 {
			zeros += 1
		}
		if report[position] == 1 {
			ones += 1
		}
	}
	if ones > zeros {
		return 0
	} else {
		return 1
	}
}

func BinaryArrayToDecimal(nums []int) int64 {
	s := ""
	for i := range nums {
		if nums[i] == 0 {
			s += "0"
		} else {
			s += "1"
		}
	}

	decimal_num, err := strconv.ParseInt(s, 2, 64)

	if err != nil {
		panic(err)
	}
	return decimal_num
}

func BitsInColumn(reports [][]int, position int) []int {
	var data []int
	for _, report := range reports {
		data = append(data, report[position])
	}
	return data
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

	var reports [][]int

	for scanner.Scan() {
		line := scanner.Text()
		report := make([]int, len(line))
		for i := range line {
			byteToInt, _ := strconv.Atoi(string(line[i]))
			report[i] = byteToInt
		}
		reports = append(reports, report)
	}

	var gamma []int
	for i := 0; i <= len(reports[0])-1; i++ {
		gamma = append(gamma, MostCommonInColumn(reports, i))
	}

	var epsilon []int
	for i := 0; i <= len(reports[0])-1; i++ {
		epsilon = append(epsilon, LeastCommonInColumn(reports, i))
	}

	gamma_decimal := BinaryArrayToDecimal(gamma)

	epsilon_decimal := BinaryArrayToDecimal(epsilon)

	fmt.Println("day 3 part 1:", gamma_decimal*epsilon_decimal)

	data := reports[:]
	for i, _ := range data {
		if len(data) == 1 {
			break
		}
		num_ones := MemberCount(data, i, 1)
		num_zeros := MemberCount(data, i, 0)
		//fmt.Println("num_ones:", num_ones)
		//fmt.Println("num_zeros:", num_zeros)
		if num_zeros > num_ones {
			data = GenericFilter(data, i, 0)
			//fmt.Println(data)
		} else {
			data = GenericFilter(data, i, 1)
			//fmt.Println(data)
		}
	}

	oxygen_generator_rating := BinaryArrayToDecimal(data[0])
	//fmt.Println("oxygen generation rating:", oxygen_generator_rating)

        data = reports[:]
        for i, _ := range data {
                if len(data) == 1 {
                        break
                }
                num_ones := MemberCount(data, i, 1)
                num_zeros := MemberCount(data, i, 0)
//                fmt.Println("num_ones:", num_ones)
//                fmt.Println("num_zeros:", num_zeros)
                if num_ones < num_zeros {
                        data = GenericFilter(data, i, 1)
//                        fmt.Println(data)
                } else {
                        data = GenericFilter(data, i, 0)
//                        fmt.Println(data)
                }
        }

        scrubber_rating := BinaryArrayToDecimal(data[0])
        //fmt.Println("scrubber rating:", scrubber_rating)

	fmt.Println("day 3 part 2:", oxygen_generator_rating * scrubber_rating)
}
