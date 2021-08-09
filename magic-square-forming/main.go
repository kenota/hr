package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func abs(num int32) int32 {
	if num < 0 {
		return -num
	}
	return num
}

func cost(a [][]int32, b [][]int32) int32 {
	var res int32 = 0

	for i := range a {
		for j := range a[i] {
			res += abs(a[i][j] - b[i][j])
		}
	}

	return res
}

func isMagic(s [][]int32) bool {
	digits := map[int32]bool{}

	for i := 0; i < len(s); i++ {
		if s[i][0]+s[i][1]+s[i][2] != 15 {
			return false
		}
		if s[0][i]+s[1][i]+s[2][i] != 15 {
			return false
		}
		for j := 0; j < len(s[i]); j++ {
			digits[s[i][j]] = true
		}
	}

	return len(digits) == 9 &&
		s[0][0]+s[1][1]+s[2][2] == 15 &&
		s[0][2]+s[1][1]+s[2][0] == 15
}

func decent(data []int32, idx int, used map[int]bool, f func(data []int32) bool) bool {
	if idx >= len(data) {
		return f(data)
	}

	for i := 1; i <= 9; i++ {
		if _, ok := used[i]; ok {
			continue
		}

		used[i] = true
		data[idx] = int32(i)

		if decent(data, idx+1, used, f) {
			return true
		}

		delete(used, i)
	}

	return false
}

// Complete the formingMagicSquare function below.
func formingMagicSquare(s [][]int32) int32 {
	var res int32 = -1

	space := []int32{0, 0, 0, 0, 0, 0, 0, 0, 0}
	used := map[int]bool{}

	if isMagic(s) {
		return 0
	}

	validate := func(nums []int32) bool {
		candidate := [][]int32{
			nums[0:3],
			nums[3:6],
			nums[6:9],
		}

		if isMagic(candidate) {
			newCost := cost(candidate, s)
			if newCost < res || res == -1 {
				res = newCost
			}
			if res == 1 {
				return true
			}
		}

		return false
	}

	decent(space, 0, used, validate)

	return res
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	var s [][]int32
	for i := 0; i < 3; i++ {
		sRowTemp := strings.Split(readLine(reader), " ")

		var sRow []int32
		for _, sRowItem := range sRowTemp {
			sItemTemp, err := strconv.ParseInt(sRowItem, 10, 64)
			checkError(err)
			sItem := int32(sItemTemp)
			sRow = append(sRow, sItem)
		}

		if len(sRow) != 3 {
			panic("Bad input")
		}

		s = append(s, sRow)
	}

	result := formingMagicSquare(s)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
