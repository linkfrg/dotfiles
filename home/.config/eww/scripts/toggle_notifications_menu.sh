#!/bin/bash

state=$(eww get open_notifications_menu)

open_notifications_menu() {
    eww open notifications_menu
    eww update open_notifications_menu=true
}

close_notifications_menu() {
    eww update open_notifications_menu=false
}

case $state in
    true)
        close_notifications_menu;;
    false)
        open_notifications_menu;;
esac