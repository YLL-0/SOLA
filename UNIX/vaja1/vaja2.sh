#!/bin/bash

cd /home/yllo/UNIX || exit
# || exit je kot OR , ki pomeni, da ce prvi del ne uspe, se izvede drugi del

cat example.txt

grep powerful example.txt

