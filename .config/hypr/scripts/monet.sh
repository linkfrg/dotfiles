#!/bin/bash
SCRIPT=~/.config/hypr/scripts/monet
source $SCRIPT/wallpaper.sh
sleep 2
pkill cava
pkill waybar
waybar &
source $SCRIPT/hyprland.sh
source $SCRIPT/mako.sh
source $SCRIPT/gtk.sh