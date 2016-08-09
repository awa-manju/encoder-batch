#!/bin/bash

. $(dirname $0)/slack_webhook.sh

REC_DATA=$1
LS_REC_DATA=$(ls -lh $REC_DATA | awk -F' ' '{print $5}' | tr -d '[:space:]')
REC_DATA_BASE=$(basename $REC_DATA)
REC_JSON="$2"
DST_DIR=/mnt/archive/ts/recorded
BACKUP_DIR=/mnt/archive/ts/backup
REC_TITLE="$(echo $REC_JSON | jq '.title' | tr [:space:] '_' | tr -d '"' | sed -e 's/_$//')"

mv $REC_DATA $DST_DIR/$REC_DATA_BASE.tmp
mv $DST_DIR/$REC_DATA_BASE.tmp $DST_DIR/$REC_DATA_BASE
echo "$REC_JSON" > $DST_DIR/$REC_DATA_BASE.json

slack_post "{\"text\":\"$REC_TITLE ($LS_REC_DATA)\", \"icon_emoji\":\":vhs:\", \"username\":\"recorded\"}"

#$(dirname $0)/comskip.sh $DST_DIR/$REC_DATA_BASE && $(dirname $0)/encode.sh /mnt/archive/ts/encoding/$REC_DATA_BASE 
