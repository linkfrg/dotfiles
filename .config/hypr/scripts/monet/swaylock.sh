#!/bin/bash

source ~/.cache/wal/colors.sh

# Путь к файлу, в котором нужно выполнить замену
file_path="/home/$USER/.config/swaylock/config"

# Обычные цвета
sed -E -i "s/(line-color=[^[:space:]]*)/line-color=$foreground/g" $file_path
sed -E -i "s/(ring-color=[^[:space:]]*)/ring-color=$foreground/g" $file_path
sed -E -i "s/(inside-color=[^[:space:]]*)/inside-color=$background/g" $file_path
sed -E -i "s/(text-color=[^[:space:]]*)/text-color=$foreground/g" $file_path

# Цвета при вводе пароля
sed -E -i "s/(line-ver-color=[^[:space:]]*)/line-ver-color=$foreground/g" $file_path
sed -E -i "s/(ring-ver-color=[^[:space:]]*)/ring-ver-color=$foreground/g" $file_path
sed -E -i "s/(inside-ver-color=[^[:space:]]*)/inside-ver-color=$background/g" $file_path
sed -E -i "s/(text-ver-color=[^[:space:]]*)/text-ver-color=$foreground/g" $file_path

# Цвета при вводе неправильного пароля
sed -E -i "s/(line-wrong-color=[^[:space:]]*)/line-wrong-color=$foreground/g" $file_path
sed -E -i "s/(ring-wrong-color=[^[:space:]]*)/ring-wrong-color=$foreground/g" $file_path
sed -E -i "s/(inside-wrong-color=[^[:space:]]*)/inside-wrong-color=$background/g" $file_path
sed -E -i "s/(text-wrong-color=[^[:space:]]*)/text-wrong-color=$foreground/g" $file_path

# Цвета при очистке пароля
sed -E -i "s/(line-clear-color=[^[:space:]]*)/line-clear-color=$foreground/g" $file_path
sed -E -i "s/(ring-clear-color=[^[:space:]]*)/ring-clear-color=$foreground/g" $file_path
sed -E -i "s/(inside-clear-color=[^[:space:]]*)/inside-clear-color=$background/g" $file_path
sed -E -i "s/(text-clear-color=[^[:space:]]*)/text-clear-color=$foreground/g" $file_path

# Сегменты
sed -E -i "s/(key-hl-color=[^[:space:]]*)/key-hl-color=$background/g" $file_path
sed -E -i "s/(separator-color=[^[:space:]]*)/separator-color=$background/g" $file_path