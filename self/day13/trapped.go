package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var (
	// key depth value range
	dr       = make(map[int]int)
	maxlevel int
)

// FWScanner is the firewall scanner
type FWScanner struct {
	depth, srange, position, direction int
}

// NewFWScanner blah blah
func NewFWScanner(depth, srange int) *FWScanner {
	return &FWScanner{depth: depth,
		srange:    srange,
		position:  0,
		direction: 1}
}

func (f FWScanner) copy() *FWScanner {
	return &FWScanner{depth: f.depth,
		srange:    f.srange,
		position:  f.position,
		direction: f.direction}
}

func (f *FWScanner) move() {
	if f.position < f.srange {
		f.position += f.direction
	}
	if f.position == 0 {
		f.direction = 1
	} else if f.position == f.srange-1 {
		f.direction = -1
	}
}

func (f FWScanner) severity() int {
	return f.depth * f.srange
}

func (f FWScanner) String() string {
	var retlist []string
	for i := 0; i < f.srange; i++ {
		if i == f.position {
			retlist = append(retlist, "S")
		} else {
			retlist = append(retlist, " ")
		}
	}

	return fmt.Sprintf("[%s]", strings.Join(retlist, " "))
}

// Firewall isn't a sparse array of FWScanners
type Firewall []*FWScanner

// NewFirewall blah blah
func NewFirewall() Firewall {
	var firewall = make([]*FWScanner, maxlevel+1)
	for i := 0; i <= maxlevel; i++ {
		if r, ok := dr[i]; ok {
			firewall[i] = NewFWScanner(i, r)
		}
	}
	return firewall
}

func (fw Firewall) copy() Firewall {
	var dst = make([]*FWScanner, len(fw))
	for idx, fws := range fw {
		if fws != nil {
			dst[idx] = fws.copy()
		}
	}
	return dst
}

func (fw Firewall) String() string {
	var retlist []string

	for _, fws := range fw {
		if fws == nil {
			retlist = append(retlist, "nil")
		} else {
			retlist = append(retlist, fws.String())
		}
	}

	return fmt.Sprintf("[%s]", strings.Join(retlist, ", "))
}

// if go had sum types, i'd return something like
// datatype severityorcollision = Severity of int | Collision of bool
// alas.
func (fw Firewall) advance(packetlevel int, reportcollision bool) int {
	severity := 0
	for idx, fws := range fw {
		if fws != nil {
			if packetlevel == idx && fws.position == 0 {
				if reportcollision {
					return 1
				}
				severity += fws.severity()
			}
			fws.move()
		}

	}
	return severity
}

func (fw Firewall) traverse(packetlevel int, reportcollision bool) (int, int) {
	retval := fw.advance(packetlevel, reportcollision)

	return retval, packetlevel + 1
}

func one() int {
	firewall := NewFirewall()
	var packetlevel, severity, s int

	for packetlevel <= maxlevel {
		s, packetlevel = firewall.traverse(packetlevel, false)
		severity += s
	}
	return severity
}

func two() int {
	var packetlevel, delay, s int
	var failed bool
	firewall := NewFirewall()
	var saved = firewall.copy()

	for {
		packetlevel = 0
		failed = false

		if delay > 0 {
			firewall.advance(-1, false)
			saved = firewall.copy()
		}

		for packetlevel <= maxlevel {
			s, packetlevel = firewall.traverse(packetlevel, true)
			if s == 1 {
				failed = true
				if delay%100000 == 0 {
					log.Printf("failed at delay %d", delay)
				}
				break
			}
		}

		if !failed {
			return delay
		}
		firewall = saved.copy()
		delay++
	}
}

func main() {
	var err error

	flag.Parse()
	if flag.NArg() == 0 {
		log.Fatal("missing input filename")
	}

	infile, err := os.Open(flag.Arg(0))
	if err != nil {
		log.Fatal(err)
	}

	defer infile.Close()

	var d, r int

	scanner := bufio.NewScanner(infile)
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), ": ")
		if d, err = strconv.Atoi(parts[0]); err != nil {
			log.Fatal(err)
		}
		if r, err = strconv.Atoi(parts[1]); err != nil {
			log.Fatal(err)
		}
		dr[d] = r
		if d > maxlevel {
			maxlevel = d
		}
	}

	log.Println(one())
	log.Println(two())
}
