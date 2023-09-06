#!/bin/bash

state=$(eww get open_powermenu)

open_powermenu() {
    eww update open_powermenu=true
}

close_powermenu() {
    eww update open_powermenu=false
}

case $state in
    true)
        close_powermenu;;
    false)
        open_powermenu;;
esac