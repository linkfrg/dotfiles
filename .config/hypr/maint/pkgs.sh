#!/bin/bash

#check if $1 is full
if [ -z "$1" ]; then
    echo "Usage: update.sh <package_manager> (e.g. pacman, yay)"
    package_manager="yay"
    echo "Defaulting to $package_manager"
else
    package_manager=$1
fi

sudo grep -vE '^\s*#|^\s*$' $HOME/.config/hypr/maint/dependencies.txt | $package_manager -Sy - --noconfirm --needed
