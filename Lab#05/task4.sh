#!/bin/bash

range=$#
i=1

while [ $i -le $range ]; do
    echo "Parameter $i: ${!i}"
    i=$((i+1))
done

until [ $i -gt $range ]; do
    echo "Parameter $i: ${!i}"
    i=$((i+1))
done
