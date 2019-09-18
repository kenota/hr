package main

import (
	"bufio"
	"os"
	"testing"
)

func TestMatchingStringsSample(t *testing.T) {
	f, err := os.Open("data/sample3")
	if err != nil {
		t.Fail()
	}
	reader := bufio.NewReaderSize(f, 1024)

	strings := readStringArray(reader)
	queries := readStringArray(reader)

	expectedResult := []int32{1, 3, 4, 3, 2}
	result := matchingStrings(strings, queries)

	for i, v := range expectedResult {
		if int(i) > len(result)+1 || v != result[i] {
			t.Fatalf("Expected result: %v != returnd result: %v", expectedResult, result)
		}
	}
}
