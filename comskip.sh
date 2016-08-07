#!/bin/bash

. $(dirname $0)/slack_webhook.sh

LOCKFILE=/tmp/comskip.lock
VIDEOFILE="$1"
JSONFILE=$VIDEOFILE.json
TIMESTAMP=$(date -r $VIDEOFILE "+%m%d%H%M")
DIRNAME=$(dirname $VIDEOFILE)
BASENAME="$(basename -s .m2ts $VIDEOFILE)"
MOVETO=/mnt/archive/ts/encoding
FAILTO=/mnt/archive/ts/failed
BACKUPTO=/mnt/archive/ts/backup
WORKDIR=/mnt/archive/ts/comskipping
CMD="ruby /opt/comskip_batch/ComskipBatch.rb"

if [ -e $LOCKFILE ];then
  echo "lockfile exists...: $LOCKFILE"
  exit 1
fi

touch $LOCKFILE

if ! echo $VIDEOFILE | grep -E 'GR26|GR27|BS101|BS102|BS103|BS191|BS192|BS193' > /dev/null; then
  $CMD \
  --margin 3 \
  --file $VIDEOFILE \
  --move_to $WORKDIR \
  --failed_to $FAILTO

  COMSKIP_RESULT=$?
  if [ $COMSKIP_RESULT -ne 0 ];then
    mv "$VIDEOFILE" "$MOVETO/$BASENAME.m2ts.tmp"
    mv "$MOVETO/$BASENAME.m2ts.tmp" "$MOVETO/$BASENAME.m2ts"
  fi
else
  mv "$VIDEOFILE" "$WORKDIR"
fi

mv "$WORKDIR/$BASENAME.m2ts.bak" "$BACKUPTO/$BASENAME.m2ts.bak"
mv "$WORKDIR/$BASENAME.m2ts" "$MOVETO/$BASENAME.m2ts.tmp"
mv "$MOVETO/$BASENAME.m2ts.tmp" "$MOVETO/$BASENAME.m2ts"

if [ -e $JSONFILE ]; then
  VIDEOTITLE=$(jq .title $JSONFILE | tr [:space:] '_' | tr -d '"' | sed -e 's/_$//')
  slack_post "{\"text\":\"comskip finished: $(expr $SECONDS / 60) mins\n$VIDEOTITLE\n$RETURN_VALUE\", \"icon_emoji\":\":clapper:\"}"
else
  slack_post "{\"text\":\"comskip finished: $(expr $SECONDS / 60) mins\n$VIDEOFILE\", \"icon_emoji\":\":clapper:\"}"
fi

mv "$DIRNAME/$BASENAME.m2ts.chapters.xml" $MOVETO
mv "$DIRNAME/$BASENAME.m2ts.avs" $MOVETO
mv "$DIRNAME/$BASENAME.txt" $MOVETO
mv "$DIRNAME/$BASENAME.vdr" $MOVETO
mv "$DIRNAME/$BASENAME.log" $MOVETO
mv "$DIRNAME/$BASENAME.m2ts.json" $MOVETO
#touch -t $TIMESTAMP "$MOVETO/$BASENAME.m2ts"

rm -f $LOCKFILE
logger $LOCKFILE removed
