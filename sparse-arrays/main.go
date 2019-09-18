package main

import (
	"bufio"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

// Complete the matchingStrings function below.
func matchingStrings(strings []string, queries []string) []int32 {
	var res = make([]int32, len(queries))

	for i, query := range queries {
		cnt := int32(0)
		for _, candidate := range strings {
			if query == candidate {
				cnt++
			}
		}
		res[i] = cnt
	}

	return res
}

// readStringArray reads reader line by line expecting following structure:
// n - number of following strings
// s1 - first string
// ..
// sn - nth string
func readStringArray(reader *bufio.Reader) []string {
	var (
		cnt int64
		err error
		res []string
		s   string
	)

	cnt, err = strconv.ParseInt(readLine(reader), 10, 32)
	checkError(err)

	for i := 0; i < int(cnt); i++ {
		s = readLine(reader)
		res = append(res, s)
	}

	return res
}

func main() {
	var (
		err              error
		stdout           *os.File
		reader           *bufio.Reader
		strings, queries []string
	)

	reader = bufio.NewReaderSize(os.Stdin, 1024*1024)
	envOut := os.Getenv("OUTPUT_PATH")
	if envOut == "" {
		stdout, err = ioutil.TempFile("", "sparse-array")
	} else {
		stdout, err = os.Create(envOut)
	}

	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	strings = readStringArray(reader)
	queries = readStringArray(reader)

	res := matchingStrings(strings, queries)

	for i, resItem := range res {
		fmt.Fprintf(writer, "%d", resItem)

		if i != len(res)-1 {
			fmt.Fprintf(writer, "\n")
		}
	}

	fmt.Fprintf(writer, "\n")

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
