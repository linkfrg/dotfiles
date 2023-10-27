#!/bin/bash

state=$(eww get open_tray)

open_tray() {
    if [[ -z $(eww windows | grep '*tray') ]]; then
        eww open tray
    fi
    eww update open_tray=true
}

close_tray() {
    eww update open_tray=false
}

case $1 in
    close)
        close_tray
        exit 0;;
esac

case $state in
    true)
        close_tray;;
    false)
        open_tray;;
esac