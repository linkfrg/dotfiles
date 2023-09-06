#!/bin/bash

~/.config/eww/scripts/get_clipboard_history.py &

if [[ -z $(eww windows | grep '*clipboard') ]]; then
    eww open clipboard
elif [[ -n $(eww windows | grep '*clipboard') ]];then
    eww close clipboard
fi