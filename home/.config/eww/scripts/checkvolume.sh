#!/bin/bash

vol="$(eww get volume)"

if [[ -z $(eww windows | grep '*osd') ]]; then
  eww open osd
fi

while true; do
  sleep 2.5

  new_vol=$(eww get volume)

  if [ "$vol" != "$new_vol" ]; then
    vol="$new_vol"
  else
    newest_vol=$(eww get volume)
    if [ "$vol" == "$newest_vol" ]; then
      if [[ -n $(eww windows | grep '*osd') ]];then
        eww close osd;
        exit
      fi
    fi
  fi
done