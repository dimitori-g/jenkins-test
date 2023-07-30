#!/bin/bash

path_to=tests

files=($(ls $path_to | grep test_))

cd $path_to

if [ "$#" -eq 0 ];
then
  for file in ${files[@]}; do
    echo ${file}
  done
elif [ "$#" -lt 1 ];
then
  for file in ${files[@]}; do
    echo ${file}
  done
  pytest $1 --deviceName=$2
else
  pytest $1 --deviceName=$2
fi