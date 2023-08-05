#!/bin/bash

source ~/.cache/wal/colors.sh

# Путь к файлу, в котором нужно выполнить замену
file_path="/home/$USER/.config/mako/config"

# Выполняем замену строки в файле
sed -E -i "s/(background-color=[^[:space:]]*)/background-color=$background/g" $file_path
sed -E -i "s/(text-color=[^[:space:]]*)/text-color=$foreground/g" $file_path
sed -E -i "s/(border-color=[^[:space:]]*)/border-color=$foreground/g" $file_path
sed -E -i "s/(progress-color=[^[:space:]]*)/progress-color=$foreground/g" $file_path

makoctl reload