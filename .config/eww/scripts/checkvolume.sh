#!/bin/bash

vol="$(eww get volume)"

if [[ $(eww get open_osd) == false ]]; then
  eww open osd
  eww update open_osd=true
fi

while true; do
  sleep 2.5

  new_vol=$(eww get volume)

  if [ "$vol" != "$new_vol" ]; then
    vol="$new_vol"
  else
    newest_vol=$(eww get volume)
    if [ "$vol" == "$newest_vol" ]; then
      if [[ $(eww get open_osd) == true ]];then
        eww update open_osd=false
        exit
      fi
    fi
  fi
done