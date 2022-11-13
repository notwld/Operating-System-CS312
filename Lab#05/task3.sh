#!/bin/bash

function week {
    case $1 in
        1) echo "Sunday" ;;
        2) echo "Monday" ;;
        3) echo "Tuesday" ;;
        4) echo "Wednesday" ;;
        5) echo "Thursday" ;;
        6) echo "Friday" ;;
        7) echo "Saturday" ;;
        *) echo "Invalid day number" ;;
    esac
}

week $1
