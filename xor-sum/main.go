package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// Complete the xorSequence function below.
func xorSequence(l int64, r int64) int64 {
	var (
		i, res, curr, m int64
	)

	for i = l; i <= r; i++ {
		switch m = i % 4; m {
		case 0:
			curr = i
		case 1:
			curr = 1
		case 2:
			curr = 1 + i
		case 3:
			curr = 0
		}
		if i == l {
			res = curr
		} else {
			res = res ^ curr
		}
	}

	return res
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	qTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	q := int32(qTemp)

	for qItr := 0; qItr < int(q); qItr++ {
		lr := strings.Split(readLine(reader), " ")

		l, err := strconv.ParseInt(lr[0], 10, 64)
		checkError(err)

		r, err := strconv.ParseInt(lr[1], 10, 64)
		checkError(err)

		result := xorSequence(l, r)

		fmt.Fprintf(writer, "%d\n", result)
	}

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
