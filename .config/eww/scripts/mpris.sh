#!/bin/bash

playerctl metadata -F -f '{{playerName}} {{title}} {{artist}} {{mpris:artUrl}} {{status}} {{mpris:length}}' | while read -r line; do
    name=$(playerctl metadata -f "{{playerName}}")
    title=$(playerctl metadata -f "{{title}}")
    artist=$(playerctl metadata -f "{{artist}}")
    artUrl=$(playerctl metadata -f "{{mpris:artUrl}}")
    status=$(playerctl metadata -f "{{status}}")
    length=$(playerctl metadata -f "{{mpris:length}}")
    if [[ $length != "" ]]; then
        length=$(($length / 1000000))
        length=$(echo "($length + 0.5) / 1" | bc)
    fi
    lengthStr=$(playerctl metadata -f "{{duration(mpris:length)}}")

    JSON_STRING=$( jq -n \
                --arg name "$name" \
                --arg title "$title" \
                --arg artist "$artist" \
                --arg artUrl "$artUrl" \
                --arg status "$status" \
                --arg length "$length" \
                --arg lengthStr "$lengthStr" \
                '{name: $name, title: $title, artist: $artist, artUrl: $artUrl, status: $status, length: $length, lengthStr: $lengthStr}' )
    echo $JSON_STRING
done