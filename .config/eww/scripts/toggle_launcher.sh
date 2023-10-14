#!/bin/bash

~/.config/eww/scripts/apps.py &

state=$(eww get open_launcher)

open_launcher() {
    if [[ -z $(eww windows | grep '*launcher') ]]; then
        eww open launcher
    fi
    eww update open_launcher=true
}

close_launcher() {
    eww close launcher
    eww update open_launcher=false
}

case $1 in
    close)
        close_launcher
        exit 0;;
    open)
        open_launcher
        exit 0;;
esac

case $state in
    true)
        close_launcher
        exit 0;;
    false)
        open_launcher
        exit 0;;
esac
