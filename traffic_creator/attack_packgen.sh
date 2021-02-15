#!/bin/bash

bytes=`shuf -i 150-200 -n 1`
type=(0 1 2 8)
sudo hping3 -${type[$(shuf -n1 -i 0-3)]} -c 1000 -d $bytes --fast  10.0.0.1
