#!/bin/bash

. $(dirname $0)/slack_webhook_url

slack_post (){
  JSONDATA=$1
  curl -X POST -H 'Content-type: application/json' \
    --data "$JSONDATA" \
    $WEBHOOK_URL
}
