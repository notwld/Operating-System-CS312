#!/bin/bash

path=/home/$(whoami)/Desktop/backup

if [ ! -d $path ]; then
    mkdir -v $path
fi
for file in /home/$(whoami)/*; do
    if [ -f $file ]; then
        echo $file 'copied to Desktop/Backup'
        cp $file $path
    else
        echo "$file is not a file"
    fi
done
