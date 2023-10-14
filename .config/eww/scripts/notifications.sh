#!/bin/bash

dismiss() {
    dbus-send --session --type=method_call \
        --dest=org.freedesktop.Notifications \
        /org/freedesktop/Notifications \
        org.freedesktop.Notifications.DismissPopup \
        uint32:$1
}

close() {
    dbus-send --session --type=method_call \
        --dest=org.freedesktop.Notifications \
        /org/freedesktop/Notifications \
        org.freedesktop.Notifications.CloseNotification \
        uint32:$1
}

action() {
    dbus-send --session --type=method_call \
        --dest=org.freedesktop.Notifications \
        /org/freedesktop/Notifications \
        org.freedesktop.Notifications.InvokeAction \
        uint32:$1 string:$2
}

clear_all() {
    dbus-send --session --type=method_call \
        --dest=org.freedesktop.Notifications \
        /org/freedesktop/Notifications \
        org.freedesktop.Notifications.ClearAll
}

get_current() {
    dbus-send --session --type=method_call \
        --dest=org.freedesktop.Notifications \
        /org/freedesktop/Notifications \
        org.freedesktop.Notifications.GetCurrent
}

get_dnd() {
    dbus-send --session --type=method_call \
        --dest=org.freedesktop.Notifications \
        /org/freedesktop/Notifications \
        org.freedesktop.Notifications.GetDNDState
}

toggle_dnd() {
    dbus-send --session --type=method_call \
        --dest=org.freedesktop.Notifications \
        /org/freedesktop/Notifications \
        org.freedesktop.Notifications.ToggleDND
}

if [[ $1 == 'dismiss' ]]; then dismiss $2 $3; fi
if [[ $1 == 'close' ]]; then close $2; fi
if [[ $1 == 'action' ]]; then action $2 $3; fi
if [[ $1 == 'clear' ]]; then clear_all; fi
if [[ $1 == 'current' ]]; then get_current; fi
if [[ $1 == 'getdnd' ]]; then get_dnd; fi
if [[ $1 == 'togglednd' ]]; then toggle_dnd && get_dnd; fi