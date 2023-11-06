#!/bin/bash

notify-send "Recording started"

file="$(xdg-user-dir VIDEOS)/$(date '+%F_%T_%:::z.mp4')"


case $1 in
    no_audio)
        wf-recorder -f $file -x yuv420p;;
    audio)
        wf-recorder -f $file -x yuv420p --audio;;
    region)
        case $2 in
            no_audio)
                wf-recorder -f $file -x yuv420p -g "$(slurp)";;
            audio)
                wf-recorder -f $file -x yuv420p --audio -g "$(slurp)";;
        esac
esac