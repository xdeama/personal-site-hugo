#!/bin/bash

# -m triggers hugo --minify
# -n exposes hugo dev server to network

EXPOSE_NETWORK=false
MINIFY=false

while getopts 'nm' flag; do
  case "${flag}" in
    n) EXPOSE_NETWORK=true ;;
    m) MINIFY=true ;;
    *) error "Unexpected option ${flag}" ;;
  esac
done

if [ "$EXPOSE_NETWORK" = "true" ]; then
    IPADDR="$(ipconfig getifaddr en0)"
    echo "hugo starting on $IPADDR:1313 (network exposed)"
    HUGO_BIND="$IPADDR"
else
    echo "hugo starting on 127.0.0.1:1313 (local only, use -n flag to expose to local network en0)"
    HUGO_BIND="127.0.0.1"
fi

export HUGO_BIND

cd hugo || exit

HUGO_SERVER_CMD="hugo server --buildDrafts --disableFastRender --bind $HUGO_BIND --baseURL http://$HUGO_BIND:1313"

if [ "$MINIFY" = "true" ]; then
    HUGO_SERVER_CMD="$HUGO_SERVER_CMD --minify"
fi

eval $HUGO_SERVER_CMD

echo "hugo stopped on $HUGO_BIND:1313"
