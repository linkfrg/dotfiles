#!/bin/bash

signal=$(nmcli -f in-use,signal dev wifi | rg "\*" | awk '{ print $2 }')
essid=$(nmcli -t -f NAME connection show --active | head -n1 | sed 's/\"/\\"/g')
echo '{"essid": "'"$essid"'", "signal": "'"$signal"'"}'

ip monitor link | while read -r line; do
    signal=$(nmcli -f in-use,signal dev wifi | rg "\*" | awk '{ print $2 }')
    essid=$(nmcli -t -f NAME connection show --active | head -n1 | sed 's/\"/\\"/g')
    echo '{"essid": "'"$essid"'", "signal": "'"$signal"'"}'
done