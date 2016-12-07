#!/bin/sh

GIST=https://gist.githubusercontent.com/seanshahkarami/9fee74fb074da6a97199b4f728e930e5/raw/9d802a5f0cd7618aad88a8dcf31741c8a7c6bac8/Report
ssh "node$1" "curl -s $GIST | sh"
