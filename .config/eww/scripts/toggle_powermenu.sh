#!/bin/bash

if [[ -z $(eww windows | grep '*powermenu') ]]; then
    eww open powermenu
elif [[ -n $(eww windows | grep '*powermenu') ]];then
    eww close powermenu
fi