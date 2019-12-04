package main

import (
	"fmt"
	"strconv"
	"strings"
)

func isPassword(pass string) bool {
	isDouble := false
	isNotDecreasing := true
	for i, char := range pass {
		if i > 0 && pass[i - 1] == uint8(char) {
			isDouble = true
		}
		if i < len(pass) - 1 && int(char) > int(pass[i + 1]) {
			isNotDecreasing = false
		}
	}
	return isDouble && isNotDecreasing
}

func isPassword2(pass string) bool {
	isDouble := false
	isNotDecreasing := true
	var triples []uint8
	var doubles []uint8
	for i, char := range pass {
		if i > 0 && pass[i - 1] == uint8(char) {
			isDouble = true
			doubles = append(doubles, uint8(char))
		}
		if i > 1 && pass[i - 1] == uint8(char) && pass[i - 2] == uint8(char) {
			triples = append(triples, uint8(char))
		}
		if i < len(pass) - 1 && int(char) > int(pass[i + 1]) {
			isNotDecreasing = false
		}
	}

	if len(triples) > 2 {
		return false
	}
	if len(triples) == 2 && triples[0] != triples[1] {
		return false
	}
	if isDouble && isNotDecreasing {
		if len(triples) == 0 {
			return true
		} else if len(triples) == 1 || (len(triples) == 2 && triples[0] == triples[1]) {
			for _, dub := range doubles {
				for _, trip := range triples {
					if dub != trip {
						return true
					}
				}
			}
		}
	}
	return false
}

func main() {
	password := "206938-679128"
	passwordRange := strings.Split(password, "-")
	validPasswords := 0

	begin, err := strconv.Atoi(passwordRange[0])
	if err != nil {
		panic(err)
	}
	end, err := strconv.Atoi(passwordRange[1])
	if err != nil {
		panic(err)
	}
	for i := begin; i < end; i++ {
		if isPassword2(strconv.Itoa(i)) {
			validPasswords++
		}
	}
	fmt.Printf("%d", validPasswords)
}
