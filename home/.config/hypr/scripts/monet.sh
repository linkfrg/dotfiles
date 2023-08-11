#!/bin/bash

# Select file
FILE=$(swayimg ~/.wallpaper/ -e "echo '%' && pkill swayimg")

# if nothing selected then exit
if [$FILE -eq ""]; then
    exit 0
fi

# generate colorscheme
wal -i $FILE -n -q -t

# set selected wallpaper
swww img $FILE --transition-fps 75 --transition-type wipe --transition-duration 2

# sleep 2 seconds to avoid lags when setting wallpaper
sleep 2

# kill cava & restart waybar
pkill cava
pkill waybar
waybar &

# restart mako
makoctl reload

# reset gtk theme
gsettings set org.gnome.desktop.interface gtk-theme Adwaita
gsettings set org.gnome.desktop.interface gtk-theme Monet


source ~/.config/hypr/scripts/wal-telegram --wal -t