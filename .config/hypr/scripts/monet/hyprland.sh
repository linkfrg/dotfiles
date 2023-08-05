#!/bin/bash
source ~/.cache/wal/colors.sh
echo "$"background"=rgb($background)" | sed 's/#//' > ~/.config/hypr/colors.conf
echo "$"foreground"=rgb($foreground)" | sed 's/#//' >> ~/.config/hypr/colors.conf