#!/bin/bash

notify-send "Начата запись экрана"

datetime=$(date | sed 's/ /_/g')

video_folder_dir=$(xdg-user-dir VIDEOS)

file="$video_folder_dir/$datetime.mp4"
wf-recorder -f $file -c libx264rgb