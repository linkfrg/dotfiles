#!/bin/bash
pkill eww
eww daemon
eww open bar
eww open bg_widgets
eww open notifications_popup
~/.config/eww/scripts/notifications.py &