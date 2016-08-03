#!/bin/bash

LOCKFILE=/tmp/ffmpeg_encode.lock
VIDEOFILE="$1"
JSONFILE=$VIDEOFILE.json
TIMESTAMP=$(date -r $VIDEOFILE "+%m%d%H%M")
echo $TIMESTAMP
DIRNAME="$(dirname $VIDEOFILE)"
BASENAME="$(basename -s .m2ts $VIDEOFILE)"
MOVETO=/mnt/share/videos
BACKUPTO=/mnt/archive/ts/backup
CMD="ffmpeg"
#CMD_OPT="-i $VIDEOFILE -passlogfile /tmp/$BASENAME.log -s 1280x720 $DIRNAME/$BASENAME.mp4"

if [ -e $LOCKFILE ];then
  echo "lockfile exists...: $LOCKFILE"
  exit 1
fi

touch $LOCKFILE

$CMD \
-y -i $VIDEOFILE \
-preset:v veryfast -b:v 2M \
-passlogfile /tmp/$BASENAME.log \
$DIRNAME/$BASENAME.mp4

touch -t $TIMESTAMP "$DIRNAME/$BASENAME.mp4"
mv "$DIRNAME/$BASENAME.m2ts" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.m2ts.chapters.xml" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.m2ts.avs" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.m2ts.bak" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.txt" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.vdr" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.log" "$BACKUPTO"

if [ -e $JSONFILE ]; then
  VIDEOTITLE=$(jq .title $JSONFILE | tr [:space:] '_' | tr -d '"' | sed -e 's/_$//')
  mv "$DIRNAME/$BASENAME.mp4" "$MOVETO/$BASENAME-$VIDEOTITLE.mp4"
else
  mv "$DIRNAME/$BASENAME.mp4" "$MOVETO"
fi

mv "$DIRNAME/$BASENAME.m2ts.json" "$BACKUPTO"

rm -f $LOCKFILE
