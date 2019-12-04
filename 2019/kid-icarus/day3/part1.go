package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"strconv"
	"strings"
)

const (
	intersection = 3
)

type Segment struct {
	distance int
	axis int // x = 1, y = -1
	direction int // pos = 1 neg = -1
}

func makeDirection(dir string) int {
	switch dir {
	case "R": return 1
	case "L": return -1
	case "D": return -1
	case "U": return 1
	}
	return 0
}

func makeAxis(dir string) int {
	switch dir {
	case "R": return 1
	case "L": return 1
	case "D": return -1
	case "U": return -1
	}
	return 0
}

func makeSegment(dir string) Segment {
	direction := makeDirection(string(dir[0]))
	axis := makeAxis(string(dir[0]))
	distance, err := strconv.Atoi(dir[1:])
	if err != nil {
		panic(err)
	}
	return Segment{distance, axis, direction}
}

func makeWire(dirs []string) []Segment {
	wire := make([]Segment, len(dirs))
	for i, dir := range dirs {
		wire[i] = makeSegment(dir)
	}
	return wire
}

func placeWire(wire []Segment, grid [][]int, lineNum int) [][]int {
	x := len(grid) / 2
	y := len(grid) / 2
	for _, segment := range wire {
		if grid[x][y] != 0 && grid[x][y] != lineNum {
			grid[x][y] = intersection
		}
		// if axis is y -1, and dir is pos, y = y - 1
		for i := 0; i < segment.distance; i++ {
			if (segment.axis == -1) {
				y += segment.direction
			} else {
				x += segment.direction
			}
			if grid[x][y] != 0 && grid[x][y] != lineNum {
				grid[x][y] = intersection
			} else {
				grid[x][y] = lineNum
			}
		}
	}
	return grid
}

func getIntersections(grid [][]int) [][]int {
	var intersects [][]int
	for i, y := range grid {
		for j, _ := range y {
			if grid[i][j] == intersection {
				intersects = append(intersects, []int{i, j})
			}
		}
	}
	return intersects
}

func findClosest(intersects [][]int, grid [][]int) float64 {
	x := len(grid) / 2
	y := len(grid) / 2
	distance := math.Inf(1)
	for _, intersection  := range intersects {
		newDistance := manhattanDistance([]int{x, y}, intersection)
		if newDistance < distance {
			distance = newDistance
		}
	}
	return distance
}

func manhattanDistance(p1 []int, p2 []int) float64 {
	return math.Abs(float64(p1[0] - p2[0])) + math.Abs(float64(p1[1] - p2[1]));
}

func calcLengthOfWireForIntersection(wire []Segment, currIntersection []int, grid [][]int) int {
	x := len(grid) / 2
	y := len(grid) / 2
	wireLength := 0
	for _, segment := range wire {
		// if axis is y -1, and dir is pos, y = y - 1
		for i := 0; i < segment.distance; i++ {
			if x == currIntersection[0] && y == currIntersection[1] {
				return wireLength
			}
			if segment.axis == -1 {
				y += segment.direction
			} else {
				x += segment.direction
			}
			wireLength++
		}
	}
	return wireLength
}

func findShortestLine(wires [][]Segment, intersections [][]int, grid [][]int) float64 {
	var wireLengths [][]int
	fmt.Println(intersections)
	for _, intersect := range intersections {
		wireLengths = append(wireLengths, []int{
			calcLengthOfWireForIntersection(wires[0], intersect, grid),
			calcLengthOfWireForIntersection(wires[1], intersect, grid),
		})
	}
	fmt.Println(len(wireLengths))
	fmt.Println(len(intersections))
	shortest := math.Inf(1)
	for _, wireLength := range wireLengths {
		totalLength := float64(wireLength[0] + wireLength[1])
		if totalLength < shortest {
			shortest = totalLength
		}
	}
	return shortest
}

func main () {
	pwd, _ := os.Getwd()
	raw, err := ioutil.ReadFile(pwd + "/part1.txt")
	if err != nil {
		panic(err)
	}
	inputStr := string(raw)
	inputLines := strings.Fields(inputStr)
	lines := make([][]string, 2)
	for i, line := range inputLines {
		segments := strings.Split(line, ",")
		lines[i] = segments
	}
	wires := make([][]Segment, 2)
	for i, wire := range lines {
		wires[i] = makeWire(wire)
	}
	grid := make([][]int, 30000)
	for i, _ := range grid {
		grid[i] = make([]int, 30000)
	}
	grid = placeWire(wires[0], grid, 1)
	grid = placeWire(wires[1], grid, 2)
	intersections := getIntersections(grid)
	//fmt.Println(findClosest(intersections, grid))
	fmt.Println(findShortestLine(wires, intersections, grid))
}
