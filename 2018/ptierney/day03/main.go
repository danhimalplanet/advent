package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
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

// a square inch of fabric
type FabricSquare struct {
	Claims []*Claim
}

type Claim struct {
	ID     int
	X      int // number of inches from the left edge
	Y      int // number of inches from the top edge
	Width  int // number of inches in X
	Height int // number of inches in Y
}

func parseClaimLine(line string) *Claim {
	fields := strings.Fields(line)

	claim := new(Claim)

	idString := strings.TrimLeft(fields[0], "#")
	id, err := strconv.Atoi(idString)

	if err != nil {
		log.Fatal(err)
	}

	claim.ID = id

	locationTupleString := strings.TrimRight(fields[2], ":")
	locationTuple := strings.Split(locationTupleString, ",")

	x, err := strconv.Atoi(locationTuple[0])

	if err != nil {
		log.Fatal(err)
	}

	claim.X = x

	y, err := strconv.Atoi(locationTuple[1])

	if err != nil {
		log.Fatal(err)
	}

	claim.Y = y

	dimsTuple := strings.Split(fields[3], "x")

	width, err := strconv.Atoi(dimsTuple[0])

	if err != nil {
		log.Fatal(err)
	}

	claim.Width = width

	height, err := strconv.Atoi(dimsTuple[1])

	if err != nil {
		log.Fatal(err)
	}

	claim.Height = height

	return claim
}

func placeClaimOnFabric(c *Claim) {
	for i := c.X; i < c.X+c.Width; i++ {
		for j := c.Y; j < c.Y+c.Height; j++ {
			Fabric[i][j].Claims = append(Fabric[i][j].Claims, c)
		}
	}
}

var ClaimsList []*Claim

var FabricWidth int = 1000
var FabricHeight int = 1000

var Fabric [][]*FabricSquare

func main() {
	inputClaims := getInput()

	ClaimsList = make([]*Claim, 0)

	Fabric = make([][]*FabricSquare, FabricWidth)

	for i := range Fabric {
		Fabric[i] = make([]*FabricSquare, FabricHeight)
	}

	for i := 0; i < FabricWidth; i++ {
		for j := 0; j < FabricHeight; j++ {
			Fabric[i][j] = new(FabricSquare)
			Fabric[i][j].Claims = make([]*Claim, 0)
		}
	}

	for _, line := range inputClaims {
		c := parseClaimLine(line)

		ClaimsList = append(ClaimsList, c)
	}

	for _, claim := range ClaimsList {
		placeClaimOnFabric(claim)
	}

	// iterate over all the squares in the fabric, counting multiple claims

	totalOverlap := 0

	for i := 0; i < FabricWidth; i++ {
		for j := 0; j < FabricHeight; j++ {
			if len(Fabric[i][j].Claims) > 1 {
				totalOverlap += 1
			}
		}
	}

	fmt.Printf("Total Overlap: %v\n", totalOverlap)

	claimDoesOverlap := make(map[int]bool)

	for _, claim := range ClaimsList {
		claimDoesOverlap[claim.ID] = false
	}

	for i := 0; i < FabricWidth; i++ {
		for j := 0; j < FabricHeight; j++ {

			squareClaims := Fabric[i][j].Claims

			if len(squareClaims) < 2 {
				continue
			}

			for _, claim := range squareClaims {
				claimDoesOverlap[claim.ID] = true
			}
		}
	}

	for claimID, doesOverlap := range claimDoesOverlap {
		if doesOverlap == true {
			continue
		}

		fmt.Printf("Non Overlap: %v\n", claimID)
	}
}
