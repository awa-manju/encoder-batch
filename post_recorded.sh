#!/bin/bash

REC_DATA=$1
REC_DATA_BASE=$(basename $REC_DATA)
REC_JSON=$2
DST_DIR=/mnt/archive/ts/recorded

mv $REC_DATA $DST_DIR/$REC_DATA_BASE.tmp
mv $DST_DIR/$REC_DATA_BASE.tmp $DST_DIR/$REC_DATA_BASE
echo $REC_JSON > $DST_DIR/$REC_DATA_BASE.json
