#!/bin/bash

# Опции
shutdown=' Выключение'
reboot=' Перезагрузка'
lock=' Заблокировать'
suspend=' Спящий режим'
logout=' Выйти'


# Действия
chosen=$(echo -e "$lock\n$suspend\n$logout\n$reboot\n$shutdown" | rofi -dmenu -p "Питание" -theme ~/.config/rofi/powermenu.rasi)
case ${chosen} in
    $shutdown)
		systemctl poweroff
        ;;
    $reboot)
		systemctl reboot
        ;;
    $lock)
		swaylock
        ;;
    $suspend)
		swaylock && systemctl suspend
        ;;
    $logout)
		hyprctl dispatch exit 0
        ;;
esac
