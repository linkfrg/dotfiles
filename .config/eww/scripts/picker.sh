#!/bin/bash

color=$(hyprpicker)

if [[ color == "" ]]; then
    echo Selection canceled
    exit 0
fi

notify-send $color
wl-copy $color