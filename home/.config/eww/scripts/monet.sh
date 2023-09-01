#!/bin/bash

# close wallpaper selector
eww close wallpaper_selector

# file
FILE=$1

# generate colorscheme
wal -i $FILE -n -q -t

# set selected wallpaper
swww img $FILE --transition-fps 75 --transition-type wipe --transition-duration 2

# sleep 2 seconds to avoid lags when setting wallpaper
sleep 2

# restart eww
eww reload

# restart mako
makoctl reload

# reset gtk theme
gsettings set org.gnome.desktop.interface gtk-theme Adwaita
gsettings set org.gnome.desktop.interface gtk-theme Monet


source ~/.config/eww/scripts/wal-telegram --wal -t