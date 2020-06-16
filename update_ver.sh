#!/bin/bash

set -e

VER_FILE=VERSION
FILE_0="README.md"
FILE_1="LEEME.md"
FILES="${FILE_0} ${FILE_1}" 

echo "Updating version in: ${FILES}"

read VER < $VER_FILE


sed -i -e "s/version [0-9]\+\.[0-9]\+\.[0-9]\+/version ${VER}/g" \
	$FILE_0

sed -i -e "s/versión [0-9]\+\.[0-9]\+\.[0-9]\+/versión ${VER}/g" \
	$FILE_1

echo "done!"

