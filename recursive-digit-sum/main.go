package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// Complete the superDigit function below.
func superDigit(n string, k int32) int32 {
	var (
		res    int32
		tmpStr string
	)

	res = digitSum(n) * k
	if res > 10 {
		tmpStr = fmt.Sprintf("%d", res)
		res = digitSum(tmpStr)
	}

	return res
}

const batchSize = 1000

func digitSum(n string) int32 {
	var (
		res       int32
		i, strlen int
		tmpStr    string
	)

	strlen = len(n)

	if strlen > batchSize {
		res = digitSum(n[:strlen/2]) + digitSum(n[strlen/2:])
	} else {
		for i = 0; i < len(n); i++ {
			res += int32(n[i] - 48)
		}
	}

	if res > 10 {
		tmpStr = fmt.Sprintf("%d", res)
		res = digitSum(tmpStr)
	}

	return res
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	nk := strings.Split(readLine(reader), " ")

	n := nk[0]

	kTemp, err := strconv.ParseInt(nk[1], 10, 64)
	checkError(err)
	k := int32(kTemp)

	result := superDigit(n, k)

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
