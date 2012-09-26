#!/bin/bash

echo "Starting publisher"
python2 pub.py &

for i in $(seq 1 10); do
    echo "Starting subscriber $i"
    python2 sub.py $i &
done
