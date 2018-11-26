package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const (
	done   = -1
	rounds = 10000
)

// Particle blah blah
type Particle struct {
	i         int
	pos       []int
	vel       []int
	acc       []int
	destroyed bool
}

func (p Particle) String() string {
	return fmt.Sprintf("%4d <p=<%d,%d,%d> v=<%d,%d,%d> a=<%d,%d,%d>",
		p.i,
		p.pos[0], p.pos[1], p.pos[2],
		p.vel[0], p.vel[1], p.vel[2],
		p.acc[0], p.acc[1], p.acc[2])
}

func (p Particle) distance() int {
	return int(math.Abs(float64(p.pos[0])) + math.Abs(float64(p.pos[1])) + math.Abs(float64(p.pos[2])))
}

func (p Particle) collision(p2 Particle) bool {
	return p.pos[0] == p2.pos[0] && p.pos[1] == p2.pos[1] && p.pos[2] == p2.pos[2]
}

// Particles blah blah
type Particles []Particle

func (particles Particles) ok() int {
	count := 0
	for _, p := range particles {
		if !p.destroyed {
			count++
		}
	}

	return count
}

// this code is expensive
func (particles Particles) collide() int {
	var p1, p2 *Particle
	destroyed := 0

	if particles.ok() == 1 {
		return done
	}

	for i := 0; i < len(particles); i++ {
		p1 = &particles[i]
		if p1.destroyed {
			continue
		}
		for j := i + 1; j < len(particles); j++ {
			p2 = &particles[j]
			if p2.destroyed {
				continue
			}
			if p1.collision(*p2) {
				destroyed++
				p2.destroyed = true
				if !p1.destroyed {
					p1.destroyed = true
					destroyed++
				}
			}
		}
	}

	return destroyed
}

func one(particles Particles) Particle {
	closest := make(map[int]int)
	distances := make([]int, len(particles))

	for idx, p := range particles {
		distances[idx] = p.distance()
	}

	for r := 0; r < rounds; r++ {
		for idx, p := range particles {
			for i := 0; i < 3; i++ {
				p.vel[i] += p.acc[i]
				p.pos[i] += p.vel[i]
			}
			distances[idx] = p.distance()
		}
		minpar := 0
		mindis := distances[0]
		for idx := 1; idx < len(distances); idx++ {
			if distances[idx] < mindis {
				minpar = idx
				mindis = distances[idx]
			}
		}
		closest[minpar]++
	}

	particle := -1
	maxcount := -1

	for p, c := range closest {
		if c > maxcount {
			maxcount = c
			particle = p
		}
	}

	return particles[particle]
}

func two(particles Particles) int {
	collisions := 0

	for r := 0; r < rounds; r++ {
		for _, p := range particles {
			if !p.destroyed {
				for i := 0; i < 3; i++ {
					p.vel[i] += p.acc[i]
					p.pos[i] += p.vel[i]
				}
			}
		}

		collisions = particles.collide()
		if collisions == done {
			return particles.ok()
		} else if collisions > 0 {
			log.Printf("round: %6d destroyed: %3d in play: %3d", r, collisions, particles.ok())
		}

		if r%1000 == 0 {
			log.Printf("round: %6d in play: %3d", r, particles.ok())
		}
	}

	return particles.ok()
}

func readParticles(fname string) Particles {
	var particles Particles

	input, err := os.Open(fname)
	if err != nil {
		log.Fatal(err)
	}
	defer input.Close()

	scanner := bufio.NewScanner(input)

	pat := regexp.MustCompile(`p=<([-\d]+,[-\d]+,[-\d]+)>, v=<([-\d]+,[-\d]+,[-\d]+)>, a=<([-\d]+,[-\d]+,[-\d]+)>`)
	pcount := 0
	for scanner.Scan() {
		groups := pat.FindAllStringSubmatch(scanner.Text(), -1)
		particle := Particle{i: pcount, destroyed: false}
		for i := 1; i < 4; i++ {
			parts := strings.Split(groups[0][i], ",")
			// dumb
			var intparts *[]int
			switch i {
			case 1:
				intparts = &particle.pos
			case 2:
				intparts = &particle.vel
			case 3:
				intparts = &particle.acc
			}
			for j := 0; j < 3; j++ {
				thing, _ := strconv.Atoi(parts[j])
				*intparts = append(*intparts, thing)
			}
		}
		particles = append(particles, particle)
		pcount++
	}

	return particles
}

func main() {
	flag.Parse()
	if flag.NArg() != 1 {
		log.Fatal("missing input file")
	}

	particles := readParticles(flag.Arg(0))
	log.Printf("one: closest particle: %s", one(particles))

	particles = readParticles(flag.Arg(0))
	log.Printf("two: particles left after collisions: %d", two(particles))
}

// eof
