#!/bin/bash

. $(dirname $0)/tools.sh
. $(dirname $0)/slack_webhook.sh

LOG_FILE=/mnt/share/videos/queue/network.log
SRC=/mnt/share/videos/queue
FAILED=/mnt/share/videos/queue/failed

TOO_LARGE='Filtering large video'
SUCCESS='Uploaded file'

TMP_FILE=/tmp/delete_uploaded.log

for i in $(find $SRC/*.mp4)
do
  FILE_NAME=$(basename $i)
  FILE_SIZE=$(ls -lh $i | awk -F' ' '{print $5}')
  PGM_NAME=$(echo $FILE_NAME | cut -d '-' -f4)
  STATUS=$(cat $LOG_FILE | grep -F $FILE_NAME)
  if echo $STATUS | grep "$SUCCESS" > /dev/null; then
    rm $i
    echo ":ok: [SUCCESS]  $PGM_NAME" >> $TMP_FILE
  elif echo $STATUS | grep "$TOO_LARGE" > /dev/null; then
    mv $i $FAILED
    echo ":warning: [TOOLARGE] $PGM_NAME ($FILE_SIZE)" >> $TMP_FILE
  fi
done

slack_post "{\"text\": \"$(cat $TMP_FILE)\", \"username\": \"uploaded status\", \"icon_emoji\": \":outbox_tray:\"}" 

rm -f $TMP_FILE
