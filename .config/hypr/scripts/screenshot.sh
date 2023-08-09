#!/bin/bash

FILE="$(xdg-user-dir PICTURES)/$(date).png"

full_screenshot() {
	grim "$FILE" | wl-copy
	send_notification
}

region_screenshot() {
	grim -g "$(slurp)" "$FILE" | wl-copy
	send_notification
}

send_notification() {
	test -f "$FILE" && notify-send -i "$FILE" "Скриншот сохранен
${FILE}"
}

case $1 in
	full)
		full_screenshot;;
	region)
		region_screenshot;;	
esac

