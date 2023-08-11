#!/bin/bash

MODE=$(makoctl mode)

DEFAULT=󰂚
DO_NOT_DISTURB=󰂛

case $MODE in
    default)
        echo $DEFAULT;;
    do-not-disturb)
        echo $DO_NOT_DISTURB;;
esac