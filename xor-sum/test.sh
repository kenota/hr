#!/bin/bash

tmpfile=$(mktemp /tmp/test-out.XXXXXX)

for i in 1 2 3
do
    cat /dev/null > $tmpfile
    cat tests/input$i | OUTPUT_PATH=$tmpfile go run main.go

    if [[ $? -ne 0 ]]; then
        echo "Failed to run $i test. Abort"
        exit -1
    fi

    diff -w tests/expectedOutput$i $tmpfile  >/dev/null 

    if [[ $? -ne 0 ]]; then
        echo "Test $i failed"
    else 
        echo "Test $i passed"
    fi
done

rm $tmpfile
