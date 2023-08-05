#!/bin/bash

current_mode=$(makoctl mode)

case $current_mode in
    default)
        makoctl mode -s do-not-disturb;;
    do-not-disturb)
        makoctl mode -s default;;
esac