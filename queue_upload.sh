#!/bin/bash

. $(dirname $0)/tools.sh

SRC=/mnt/share/videos
DST=/mnt/share/videos/queue

list_aged_files $SRC *.mp4 4 | xargs -I{} mv {} $DST
