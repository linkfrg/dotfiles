#!/bin/sh

if [[ $1 == "on" ]]; then
    NIRI_CMD="niri msg action power-on-monitors"
    HYPRLAND_CMD="hyprctl dispatch dpms on"
else
    NIRI_CMD="niri msg action power-off-monitors"
    HYPRLAND_CMD="hyprctl dispatch dpms off"
fi


if [[ $XDG_CURRENT_DESKTOP == "niri" ]]; then
    eval $NIRI_CMD
elif [[ $XDG_CURRENT_DESKTOP == "hyprland" ]]; then
    eval $HYPRLAND_CMD
fi
