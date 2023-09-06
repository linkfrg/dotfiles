#!/bin/bash

# Set the directory path
file=$(zenity --file-selection --filename $HOME/.wallpaper/)

# Find image files (adjust the extensions as needed)
if [[ $file == "" ]]; then
    exit 0
fi

~/.config/eww/scripts/generate_colors.py -i $file --current-scheme
