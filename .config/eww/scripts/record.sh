#!/bin/bash

notify-send "Recording started"

file="$(xdg-user-dir VIDEOS)/$(date '+%F_%T_%:::z.mp4')"


case $1 in
    no_audio)
        wf-recorder -f $file -c libx264rgb;;
    audio)
        wf-recorder -f $file -c libx264rgb --audio;;
    region)
        case $2 in
            no_audio)
                wf-recorder -f $file -c libx264rgb -g "$(slurp)";;
            audio)
                wf-recorder -f $file -c libx264rgb --audio -g "$(slurp)";;
        esac
esac