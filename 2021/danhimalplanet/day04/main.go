package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func addRow(row []int) int {
	return 0
}

func IsWinnerXRows(board [][]int) bool {
	for i := 0; i < 5; i++ {
		sum := 0
		sum += board[i][0]
		sum += board[i][1]
		sum += board[i][2]
		sum += board[i][3]
		sum += board[i][4]
		if sum == 500 {
			return true
		}
	}
	return false
}

func IsWinnerYColumns(board [][]int) bool {
	for i := 0; i < 5; i++ {
		sum := 0
		sum += board[0][i]
		sum += board[1][i]
		sum += board[2][i]
		sum += board[3][i]
		sum += board[4][i]
		if sum == 500 {
			return true
		}
	}
	return false
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

	var moves []int

	var board_lines [][]int

	line_count := 0
	for scanner.Scan() {
		line := scanner.Text()
		if line_count == 0 {
			d := strings.Split(line, ",")
			for i := range d {
				j, err := strconv.Atoi(d[i])
				if err != nil {
					log.Fatal("failed to convert")
				}
				moves = append(moves, j)
			}
		} else if line != "" {
			var board_line []int
			d := strings.Split(line, " ")
			for i := range d {
				if d[i] != "" {
					j, err := strconv.Atoi(d[i])
					if err != nil {
						log.Fatal("failed to convert")
					}
					board_line = append(board_line, j)
				}
			}
			board_lines = append(board_lines, board_line)
		}
		line_count += 1
	}

	var _boards [][][]int

	counter := 0
	var _board [][]int
	for i := range board_lines {
		_board = append(_board, board_lines[i])
		if counter == 4 && i < len(board_lines) {
			_boards = append(_boards, _board)
			_board = nil
			counter = 0
		} else {
			counter += 1
		}
	}

	var boards [][][]int
	for i := range _boards {
		var board [][]int
		length := len(_boards[i])
		for j := length - 1; j >= 0; j-- {
			board = append(board, _boards[i][j])
		}
		boards = append(boards, board)

	}

	var _b [][][]int
	for i := len(boards) - 1; i >= 0; i-- {
		_b = append(_b, boards[i])
	}
	boards = _b

	var win_record []int

	found := 0
	for draw := range moves {
		for i := range boards {
			for j := 4; j >= 0; j-- {
				for k := 4; k >= 0; k-- {
					if boards[i][j][k] == moves[draw] && found == 0 {
						boards[i][j][k] = 100

						if IsWinnerXRows(boards[i]) || IsWinnerYColumns(boards[i]) {

							var result bool = false
							for _, x := range win_record {
								if x == i {
									result = true
									break
								}
							}

							if !result {
								winning_number := moves[draw]
								fmt.Println("winning number:", winning_number)
								fmt.Println("winner board:", i)
								//fmt.Println(boards[i])
								//found = 1
								sum_unmarked_numbers := 0
								for x := 0; x < 5; x++ {
									for y := 0; y < 5; y++ {
										if boards[i][x][y] != 100 {
											sum_unmarked_numbers += boards[i][x][y]
										}
									}

								}
								fmt.Println("sum_unmarked_numbers:", sum_unmarked_numbers)
								fmt.Println("final_score:", winning_number*sum_unmarked_numbers)
								win_record = append(win_record, i)
							}
						}
					}
				}
			}
		}
	}
}
