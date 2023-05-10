#!/bin/sh

which wget >/dev/null 2>&1
WGET=$?
which curl >/dev/null 2>&1
CURL=$?
if [ "$WGET" -eq 0 ]; then
    DL_CMD="wget --no-verbose -c"
elif [ "$CURL" -eq 0 ]; then
    DL_CMD="curl -C - -O"
else
    echo "You need wget or curl installed to download"
    exit 1
fi

$DL_CMD http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz
