#!/bin/bash


raise_volume() {
    pamixer --unmute
    pamixer --increase 5
    send_volume_notify
}

lower_volume() {
    pamixer --unmute
    pamixer --decrease 5
    send_volume_notify
}

send_volume_notify() {
    current_volume=$(pamixer --get-volume)
    notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -h int:value:$current_volume " "
}

toggle_mute() {
    pamixer --toggle-mute
}

case $1 in
    raise)
        raise_volume;;
    lower)
        lower_volume;;
    mute)
        toggle_mute;;
esac

