#!/bin/bash

if [ -w /bin/pwd ]
then echo 'Writable file'
else
	echo 'Not Writeable'
	cp /bin/pwd /home/notwld/Desktop
	echo 'Copied File'
	chmod ugo+w /home/notwld/Desktop/pwd
	echo 'Permission Changed!'
fi
 
