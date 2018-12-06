package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"
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

type ReposeRecord struct {
	GuardID      int
	GuardIDIsSet bool
	Timestamp    time.Time
	Event        string
}

type GuardShift struct {
	GuardID int

	Naps []*GuardNap
}

type GuardNap struct {
	NapStart        time.Time
	NapEnd          time.Time
	MinutesDuration int
}

var inputTimeLayout string = "[2006-01-02 15:04]"

func parseReposeRecordLine(line string) *ReposeRecord {
	fields := strings.Fields(line)

	rr := new(ReposeRecord)

	fullTime := fields[0] + " " + fields[1]

	t, err := time.Parse(inputTimeLayout, fullTime)

	if err != nil {
		log.Fatal(err)
	}

	rr.Timestamp = t

	if len(fields) == 4 {
		rr.GuardIDIsSet = false

		rr.Event = fields[2] + " " + fields[3]
	} else {
		rr.GuardIDIsSet = true

		idString := strings.TrimLeft(fields[3], "#")

		rr.GuardID, err = strconv.Atoi(idString)

		if err != nil {
			log.Fatal(err)
		}

		rr.Event = fields[4] + " " + fields[5]
	}

	return rr
}

var ReposeRecordList []*ReposeRecord
var GuardShiftList []*GuardShift

// sum of total naps a guard took
var GuardIDNapSums map[int]int

// Sorting Code
type ByTimestamp []*ReposeRecord

func (a ByTimestamp) Len() int           { return len(a) }
func (a ByTimestamp) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByTimestamp) Less(i, j int) bool { return a[i].Timestamp.Before(a[j].Timestamp) }

func main() {
	inputClaims := getInput()

	ReposeRecordList = make([]*ReposeRecord, 0)

	for _, line := range inputClaims {
		rr := parseReposeRecordLine(line)

		ReposeRecordList = append(ReposeRecordList, rr)
	}

	sort.Sort(ByTimestamp(ReposeRecordList))

	// set the guard IDs
	if ReposeRecordList[0].GuardIDIsSet == false {
		log.Fatal("Invalid input")
	}

	var currentGuardID int

	for _, rr := range ReposeRecordList {
		if rr.Event == "begins shift" {
			currentGuardID = rr.GuardID
			continue
		}

		rr.GuardID = currentGuardID
	}

	var currentShift *GuardShift = nil
	var currentNap *GuardNap

	for _, rr := range ReposeRecordList {
		if rr.Event == "begins shift" {
			if currentShift != nil {
				GuardShiftList = append(GuardShiftList, currentShift)
			}

			currentShift = new(GuardShift)
			currentShift.GuardID = rr.GuardID
			continue
		}

		if rr.Event == "falls asleep" {
			currentNap = new(GuardNap)
			currentNap.NapStart = rr.Timestamp
		}

		if rr.Event == "wakes up" {
			currentNap.NapEnd = rr.Timestamp

			// calculate the duration
			nanosecondsDuration := currentNap.NapEnd.Sub(currentNap.NapStart)
			currentNap.MinutesDuration = int(time.Duration.Minutes(nanosecondsDuration))

			currentShift.Naps = append(currentShift.Naps, currentNap)
		}

		rr.GuardID = currentGuardID
	}

	// add the trailing shift
	GuardShiftList = append(GuardShiftList, currentShift)

	GuardIDNapSums = make(map[int]int)

	// build up the sums of naps
	for _, gs := range GuardShiftList {
		for _, n := range gs.Naps {
			GuardIDNapSums[gs.GuardID] += n.MinutesDuration
		}
	}

	// find the guard who sleeps the most

	maxGuardID := -1
	maxNapSum := 0

	for guardID, napSum := range GuardIDNapSums {
		if maxGuardID < 0 {
			maxGuardID = guardID
			maxNapSum = napSum
			continue
		}

		if napSum < maxNapSum {
			continue
		}

		maxGuardID = guardID
		maxNapSum = napSum
	}

	var maxGuardNaps []*GuardNap = make([]*GuardNap, 0)

	for _, gs := range GuardShiftList {
		if gs.GuardID != maxGuardID {
			continue
		}

		for _, n := range gs.Naps {
			maxGuardNaps = append(maxGuardNaps, n)
		}
	}

	// keys is the minute of the day, 0-59
	// sleep only happens during the midnight hour
	var minutesSum []int = make([]int, 60)

	for _, nap := range maxGuardNaps {
		for i := nap.NapStart.Minute(); i < nap.NapEnd.Minute(); i++ {
			minutesSum[i] += 1
		}
	}

	maxMinuteIndex := 0
	maxMinuteCount := minutesSum[maxMinuteIndex]

	for i, napSum := range minutesSum {
		if napSum < maxMinuteCount {
			continue
		}

		maxMinuteIndex = i
		maxMinuteCount = napSum
	}

	fmt.Printf("Part 1:\nGuard ID: %v\nMinute: %v\n", maxGuardID, maxMinuteIndex)

	var guardMinutesMap map[int][]int = make(map[int][]int)

	for guardID, _ := range GuardIDNapSums {
		guardMinutesMap[guardID] = make([]int, 60)
	}

	for _, gs := range GuardShiftList {
		for _, nap := range gs.Naps {
			for i := nap.NapStart.Minute(); i < nap.NapEnd.Minute(); i++ {
				guardMinutesMap[gs.GuardID][i] += 1
			}
		}
	}

	maxGuardID = -1
	maxMinuteSum := 0
	maxMinuteIndex = 0

	for guardID, napMinutes := range guardMinutesMap {
		if maxGuardID < 0 {
			maxGuardID = guardID
			maxMinuteIndex = napMinutes[maxMinuteIndex]
		}

		for i, sum := range napMinutes {
			if sum < maxMinuteSum {
				continue
			}

			maxGuardID = guardID
			maxMinuteSum = sum
			maxMinuteIndex = i
		}
	}

	fmt.Printf("Part 2:\nGuard ID: %v\nMinute: %v\n", maxGuardID, maxMinuteIndex)
}
