#!/bin/bash

wallpapers=$(ls ~/.wallpaper/)

selected=$(echo -e $wallpapers | tr " " "\n" | rofi -dmenu)

if [$selected -eq ""]; then
    exit 0
fi

wal -i ~/.wallpaper/$selected -n -q -t
swww img ~/.wallpaper/$selected --transition-fps 75 --transition-type wipe --transition-duration 2
