#!/bin/bash

function file_old(){
  TODAY=$(date +%s)
  ARG1_DATE=$(date +%s -r $1)
  expr $TODAY - $ARG1_DATE
}

function days2sec(){
  expr 3600 \* 24 \* $1
}

DIR=/mnt/archive/ts/backup

for i in $(find $DIR/*); do
  if [ $(file_old $i) -gt $(days2sec 2) ]; then
    echo $i
  fi
done | xargs rm -f
