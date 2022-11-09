#!/bin/bash

age=$1
marks=$2

if  [ $age -lt '18' ]
then
	if [ $marks -gt '700' ]
	then
		echo 'Student is eligible to take admission!'
	else
		echo 'Marks should be greater than 700!'
	fi
else
	echo 'Age should be lesser than 18!'
fi
