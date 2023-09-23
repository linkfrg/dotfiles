#!/bin/bash
pkill eww
eww daemon
eww open bar
~/.config/eww/scripts/notifications.py &