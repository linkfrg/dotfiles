#!/bin/bash

[[ -z $(pgrep checkvolume.sh) ]] && ~/.config/eww/scripts/checkvolume.sh &

# requieres pamixer

case $1 in
--up)
  pamixer -u >/dev/null
  pamixer -i 5 >/dev/null
  ;;
--down)
  pamixer -u >/dev/null
  pamixer -d 5 >/dev/null
  ;;
--toggle)
  pamixer -t >/dev/null
  ;;
esac