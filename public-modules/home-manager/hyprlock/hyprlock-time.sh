#!/bin/bash

current_hour=$(date +"%H")
user_string="<span color='$primaryHex'>$USER</span>"

if [ "$current_hour" -ge 5 ] && [ "$current_hour" -lt 12 ]; then
    echo "Good morning, $user_string"
elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 18 ]; then
    echo "Good day, $user_string"
elif [ "$current_hour" -ge 18 ] && [ "$current_hour" -lt 22 ]; then
    echo "Good evening, $user_string"
else
    echo "Good night, $user_string"
fi
