#!/bin/bash

echo "Starting pusher"
python2 push.py &

for i in $(seq 1 10); do
    echo "Starting worker $i"
    python2 pull.py $i &
done
