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
	//file, err := os.Open("test_input")

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

type Point struct {
	X int
	Y int
}

var grid [][]int
var points []Point

func dist(x1, y1, x2, y2 int) int {
	xDist := x1 - x2
	yDist := y1 - y2

	if xDist < 0 {
		xDist = -xDist
	}

	if yDist < 0 {
		yDist = -yDist
	}

	return xDist + yDist
}

func closestPoint(x int, y int) int {
	closestIndex := 0
	closestDist := dist(x, y, points[0].X, points[0].Y)

	for i, p := range points {
		d := dist(x, y, p.X, p.Y)

		if d < closestDist {
			closestIndex = i
			closestDist = d
		}
	}

	return closestIndex
}

var offset int = 500
var gridBaseDim int = 1000
var gridDim int = offset + gridBaseDim

func main() {
	input := getInput()

	grid = make([][]int, gridDim)

	for i := 0; i < gridDim; i++ {
		grid[i] = make([]int, gridDim)
	}

	points = make([]Point, len(input))

	for i, line := range input {
		elems := strings.Split(line, ", ")

		x, _ := strconv.Atoi(elems[0])
		y, _ := strconv.Atoi(elems[1])

		points[i].X = x + offset
		points[i].Y = y + offset
	}

	for i := 0; i < gridDim; i++ {
		for j := 0; j < gridDim; j++ {
			grid[i][j] = closestPoint(i, j)
		}
	}

	invalidPoints := make(map[int]bool)

	for i := 0; i < gridDim; i++ {
		invalidPoints[grid[i][0]] = true
		invalidPoints[grid[i][gridDim-1]] = true
		invalidPoints[grid[0][i]] = true
		invalidPoints[grid[gridDim-1][i]] = true
	}

	areas := make(map[int]int)

	for i := 0; i < gridDim; i++ {
		for j := 0; j < gridDim; j++ {
			p := grid[i][j]

			if invalidPoints[p] == true {
				continue
			}

			areas[p] += 1
		}
	}

	maxIndex := 0
	maxArea := areas[0]

	for index, area := range areas {
		if area > maxArea {
			maxIndex = index
			maxArea = area
		}
	}

	fmt.Printf("Part 1:\nMaximum Area Index: %v\nArea: %v\n", maxIndex, maxArea)

	regionSize := 0

	for i := 0; i < gridDim; i++ {
		for j := 0; j < gridDim; j++ {
			distSum := 0

			for _, p := range points {
				distSum += dist(i, j, p.X, p.Y)
			}

			if distSum < 10000 {
				regionSize += 1
			}
		}
	}

	fmt.Printf("Part 2:\nRegion Area: %v\n", regionSize)
}
