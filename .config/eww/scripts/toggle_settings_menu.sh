#!/bin/bash

state=$(eww get open_settings_menu)

open_settings_menu() {
    eww open settings_menu
    eww update open_settings_menu=true
}

close_settings_menu() {
    eww update open_settings_menu=false
}

case $state in
    true)
        close_settings_menu;;
    false)
        open_settings_menu;;
esac