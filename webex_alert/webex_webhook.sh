#!/bin/sh

curl -X POST -H "Content-Type: application/json" -d '{"text" : "'"$WEBEX_MESSAGE"'"}' "$WEBEX_WEBHOOK"