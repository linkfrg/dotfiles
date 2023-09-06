#!/bin/bash

pamixer --get-volume-human | tr -d '%'

pactl subscribe | rg --line-buffered "on sink" | while read -r _; do
  pamixer --get-volume-human | tr -d '%'
done