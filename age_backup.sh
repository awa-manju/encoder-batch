#!/bin/bash

. $(dirname $0)/tools.sh

TS_AGE_DAYS=3
TS_DIR=/mnt/archive/ts/backup

list_aged_files $TS_DIR *.m2ts* $TS_AGE_DAYS | xargs rm -f

MP4_AGE_DAYS=3
MP4_TS_DIR=/mnt/share/videos
list_aged_files $MP4_DIR *mp4 $MP4_AGE_DAYS | xargs rm -f
