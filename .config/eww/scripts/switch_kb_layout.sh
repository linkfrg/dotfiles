#!/bin/bash
hyprctl \
  --batch "$(
    hyprctl devices -j |
      jq -r '.keyboards[] | .name' |
      while IFS= read -r keyboard; do
        printf '%s %s %s;' 'switchxkblayout' "${keyboard}" 'next'
      done
  )"

layout=$(hyprctl devices -j |
  jq -r '.keyboards[] | .active_keymap' |
  head -n1 |
  cut -c1-2 |
  tr 'A-Z' 'a-z')

eww update kb_layout=$layout