#!/bin/bash


cd /home/yllo/UNIX

mkdir vaja1

cd vaja1 || exit

touch file1.txt
touch file2.txt
touch file3.txt

ls -a

rm file1.txt
mv file3.txt renamed_file.txt

ls -a


