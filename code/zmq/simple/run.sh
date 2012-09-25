#!/bin/bash
LEN=100000
WORKERS=50
SUB_LEN=100

python2 sink.py $SUB_LEN &
python2 manager.py $LEN $WORKERS &
for i in $(seq 0 $WORKERS)
do python2 worker.py $i &
done
