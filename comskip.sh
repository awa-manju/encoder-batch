#!/bin/bash

LOCKFILE=/tmp/comskip.lock
VIDEOFILE="$1"
TIMESTAMP=$(date -r $VIDEOFILE "+%m%d%H%M")
DIRNAME=$(dirname $VIDEOFILE)
BASENAME=$(basename -s .m2ts $VIDEOFILE)
MOVETO=/mnt/videos/encoding
FAILTO=/mnt/archive/videos/failed
CMD="ruby /opt/comskip_batch/ComskipBatch.rb"

if [ -e $LOCKFILE ];then
  echo "lockfile exists...: $LOCKFILE"
  exit 1
fi

touch $LOCKFILE

$CMD \
--margin 3 \
--file $VIDEOFILE \
--move_to $MOVETO \
--failed_to $FAILTO

mv $DIRNAME/$BASENAME.* $MOVETO
touch -t $TIMESTAMP "$MOVETO/$BASENAME.m2ts"*

rm -f $LOCKFILE
