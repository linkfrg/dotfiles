#!/bin/bash

state=$(eww get open_time_menu)

open_time_menu() {
    eww open time_menu
    eww update open_time_menu=true
}

close_time_menu() {
    eww update open_time_menu=false
}

case $state in
    true)
        close_time_menu;;
    false)
        open_time_menu;;
esac