#!/bin/bash

. $(dirname $0)/tools.sh

AGE_DAYS=3
DIR=/mnt/archive/ts/backup

list_aged_files $DIR *.m2ts* $AGE_DAYS | xargs rm -f
