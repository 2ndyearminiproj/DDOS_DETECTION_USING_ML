#!/bin/bash


while true; do
	packet=`shuf -i 10-20 -n 1`
	bytes=`shuf -i 150-200 -n 1`
	pause=`shuf -i 1-10 -n 1`
	type=(0 1 2 8)
	sudo hping3 -${type[$(shuf -n1 -i 0-3)]} -c $packet -d $bytes  10.0.0.1
	sleep $pause
done
