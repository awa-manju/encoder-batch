#!/bin/bash

LOCKFILE=/tmp/ffmpeg_encode.lock
VIDEOFILE="$1"
TIMESTAMP=$(date -r $VIDEOFILE "+%m%d%H%M")
DIRNAME="$(dirname $VIDEOFILE)"
BASENAME="$(basename -s .m2ts $VIDEOFILE)"
MOVETO=/mnt/archive/videos
BACKUPTO=/mnt/archive/videos/backup
CMD="ffmpeg"
CMD_OPT="-i $VIDEOFILE -passlogfile /tmp/$BASENAME.log -s 1280x720 $DIRNAME/$BASENAME.mp4"

if [ -e $LOCKFILE ];then
  echo "lockfile exists...: $LOCKFILE"
  exit 1
fi

touch $LOCKFILE

$CMD $CMD_OPT
touch -t $TIMESTAMP "$DIRNAME/$BASENAME.mp4"
mv "$DIRNAME/$BASENAME.mp4" "$MOVETO"
mv "$DIRNAME/$BASENAME".* "$BACKUPTO"

rm -f $LOCKFILE
