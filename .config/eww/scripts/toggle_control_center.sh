#!/bin/bash

state=$(eww get open_control_center)

open_control_center() {
    if [[ -z $(eww windows | grep '*control_center') ]]; then
        eww open control_center
    fi
    eww update open_control_center=true
}

close_control_center() {
    eww update open_control_center=false
}

case $1 in
    close)
        close_control_center
        exit 0;;
esac

case $state in
    true)
        close_control_center;;
    false)
        open_control_center;;
esac