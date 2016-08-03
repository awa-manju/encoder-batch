#!/bin/bash

LOCKFILE=/tmp/comskip.lock
VIDEOFILE="$1"
TIMESTAMP=$(date -r $VIDEOFILE "+%m%d%H%M")
DIRNAME=$(dirname $VIDEOFILE)
BASENAME="$(basename -s .m2ts $VIDEOFILE)"
MOVETO=/mnt/archive/ts/encoding
FAILTO=/mnt/archive/ts/failed
CMD="ruby /opt/comskip_batch/ComskipBatch.rb"

if [ -e $LOCKFILE ];then
  echo "lockfile exists...: $LOCKFILE"
  exit 1
fi

touch $LOCKFILE

if ! echo $VIDEOFILE | grep 'GR26|GR27|BS101|BS102|BS103|BS191|BS192|BS193' > /dev/null; then
$CMD \
--margin 3 \
--file $VIDEOFILE \
--move_to $MOVETO \
--failed_to $FAILTO
fi

mv "$DIRNAME/$BASENAME.m2ts" $MOVETO
mv "$DIRNAME/$BASENAME.m2ts.json" $MOVETO
mv "$DIRNAME/$BASENAME.m2ts.chapters.xml" $MOVETO
mv "$DIRNAME/$BASENAME.m2ts.avs" $MOVETO
mv "$DIRNAME/$BASENAME.txt" $MOVETO
mv "$DIRNAME/$BASENAME.vdr" $MOVETO
mv "$DIRNAME/$BASENAME.log" $MOVETO
touch -t $TIMESTAMP "$MOVETO/$BASENAME.m2ts"

rm -f $LOCKFILE
