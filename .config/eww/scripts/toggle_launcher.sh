#!/bin/bash

~/.config/eww/scripts/apps.py &

if [[ -z $(eww windows | grep '*launcher') ]]; then
    eww open launcher
elif [[ -n $(eww windows | grep '*launcher') ]];then
    eww close launcher
fi