#!/bin/bash
direction=$1
current=$2
if [[ $direction == "down" ]]; then
    target=$(($current+1))
    if [[ $target == 11 ]]; then
        exit 0
    fi
    hyprctl dispatch workspace $target
elif [[ $direction == "up" ]]; then
    target=$(($current-1))
    hyprctl dispatch workspace $target
fi
