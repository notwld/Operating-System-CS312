#!/bin/bash

echo 'Enter string a:'
read a
echo 'Enter string b:'
read b

if [ $a = $b ]
then echo 'given strings are equal!'
else echo 'given strings are not equal!'
fi
