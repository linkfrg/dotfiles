#!/bin/bash

direction=$1
current=$2
max=$3
if [[ $direction == "down" ]]; then
    target=$(($current+1))
    if [[ $target == $max ]]; then
        exit 0
    fi
    eww update current_wallpaper=$target
elif [[ $direction == "up" ]]; then
    target=$(($current-1))
    if [[ $target == -1 ]]; then
        exit 0
    fi
    eww update current_wallpaper=$target
fi