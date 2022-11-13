#!/bin/bash

read -p "Enter your roll number: " roll

sum=0
count=0

for i in $( seq 0 $roll ); do
    if [ $((i%2)) -eq 0 ]; then
        sum=$((sum+i))
	let count=$(($count+1))
    fi
done

echo "Avg:" $((sum/count))
