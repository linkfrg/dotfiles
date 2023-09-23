#!/bin/bash


open_control_center() {
    if [[ -z $(eww windows | grep '*control_center') ]]; then
        eww open control_center
    fi
    eww update open_control_center=true
}

close_control_center() {
    eww update open_control_center=false
    eww update open_powermenu=false
}

case $1 in
    close)
        close_control_center;;
    open)
        open_control_center;;
esac