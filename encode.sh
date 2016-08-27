#!/bin/bash

. $(dirname $0)/slack_webhook.sh

LOCKFILE=/tmp/ffmpeg_encode.lock
VIDEOFILE="$1"
JSONFILE=$VIDEOFILE.json
TIMESTAMP=$(date -r $VIDEOFILE "+%m%d%H%M")
DIRNAME="$(dirname $VIDEOFILE)"
BASENAME="$(basename -s .m2ts $VIDEOFILE)"
MOVETO=/mnt/share/videos
BACKUPTO=/mnt/archive/ts/backup
QUEUETO=/mnt/share/videos/queue
CMD="ffmpeg"
#CMD_OPT="-i $VIDEOFILE -passlogfile /tmp/$BASENAME.log -s 1280x720 $DIRNAME/$BASENAME.mp4"

if [ -e $LOCKFILE ];then
  echo "lockfile exists...: $LOCKFILE"
  exit 1
fi

touch $LOCKFILE

$CMD \
-i $VIDEOFILE \
-s 1280x720 \
-preset:v veryfast \
-passlogfile /tmp/$BASENAME.log \
$DIRNAME/$BASENAME.mp4

#touch -t $TIMESTAMP "$DIRNAME/$BASENAME.mp4"
mv "$DIRNAME/$BASENAME.m2ts" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.m2ts.chapters.xml" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.m2ts.avs" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.m2ts.bak" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.txt" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.vdr" "$BACKUPTO"
mv "$DIRNAME/$BASENAME.log" "$BACKUPTO"

logger $DIRNAME/$BASENAME.m2ts finished

if [ -e $JSONFILE ]; then
  VIDEOTITLE=$(jq .title $JSONFILE | tr [:space:] '_' | tr -d '"' | sed -e 's/_$//')
  WORD='ＷＢＳ'
  if echo $VIDEOTITLE | grep $WORD > /dev/null; then
    VIDEOTITLE=$WORD
  fi
  mv "$DIRNAME/$BASENAME.mp4" "$MOVETO/$BASENAME-$VIDEOTITLE.mp4"
  cp "$MOVETO/$BASENAME-$VIDEOTITLE.mp4" "$QUEUETO/$BASENAME-$VIDEOTITLE.mp4"
  slack_post "{\"text\":\"$VIDEOTITLE ($(expr $SECONDS / 60) mins)\", \"icon_emoji\":\":iphone:\", \"username\":\"encode\"}"
else
  mv "$DIRNAME/$BASENAME.mp4" "$MOVETO"
  cp "$MOVETO/$BASENAME.mp4" "$QUEUETO"
  slack_post "{\"text\":\"$VIDEOFILE ($(expr $SECONDS / 60) mins)\", \"icon_emoji\":\":iphone:\", \"username\":\"encode\"}"
fi

logger $DIRNAME/$BASENAME.mp4 finished

mv "$DIRNAME/$BASENAME.m2ts.json" "$BACKUPTO"

rm -f $LOCKFILE
logger $LOCKFILE removed

