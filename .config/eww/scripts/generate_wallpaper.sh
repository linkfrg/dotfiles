#!/bin/bash

selected_color=$(zenity --color-selection --show-palette)

if [ $? -eq 1 ]; then
    echo "Color selection canceled."
    exit 1
fi

rgb_color=$(echo "$selected_color" | sed 's/[^0-9,]*\([0-9]*,[0-9]*,[0-9]*\).*/\1/')

IFS=',' read -ra rgb_array <<< "$rgb_color"

hex_color="#"
for component in "${rgb_array[@]}"; do
    hex_component=$(printf "%02X" "$component")
    hex_color="${hex_color}${hex_component}"
done
~/.config/eww/scripts/material.py --color $hex_color