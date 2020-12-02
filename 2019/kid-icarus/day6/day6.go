package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

type Node struct {
	name string
	children []*Node
}

func makeNode (name string, children []string) Node {
	var childNodes []*Node
	node := Node{name, nil}
	for _, name := range children {
		child := Node{name, nil}
		childNodes = append(childNodes, &child)
	}
	node.children = childNodes
	return node
}

//func insert (tree *Node, ) Node {
//
//}

func walk (tree *Node, count float64) float64 {
	if tree.children == nil {
		return count
	}

	for _, child := range tree.children {
		count = count + walk(child, count)
	}
	return count
}


func makeKids(planetMap map[string][]string, kid *Node) Node {
	for _, child := range kid.children {
		for _, name := range planetMap[child.name] {
			node := makeNode(name, planetMap[name])
			child.children = append(child.children, &node)
			makeKids(planetMap, &node)
		}
	}
	return *kid
}

func makePlanetTree(planetMap map[string][]string) Node {
	root := makeNode("COM", planetMap["COM"])
	return makeKids(planetMap, &root)
}

func main() {
	pwd, _ := os.Getwd()
	raw, err := ioutil.ReadFile(pwd + "/input.txt")
	if err != nil {
		panic(err)
	}
	input := string(raw)
	lines := strings.Fields(input)
	planetMap := make(map[string]string)
	for _, line := range lines {
		planets := strings.Split(line, ")")
		planetMap[planets[1]] = planets[0]
	}

	sum := 0
	for planet := range planetMap {
		for {
			parent, ok := planetMap[planet]
			if !ok {
				break
			}
			planet = parent
			sum++
		}
	}

	fmt.Println(sum)
}
