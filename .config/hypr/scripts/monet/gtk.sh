#!/bin/bash
source ~/.cache/wal/colors.sh

rm -R ~/.themes/*
cp -R ~/.config/hypr/scripts/monet/Catppuccin-Mocha-Standard-Blue-dark ~/.themes/
mv ~/.themes/Catppuccin-Mocha-Standard-Blue-dark ~/.themes/$selected/

GTK3_DIR=~/.themes/$selected/gtk-3.0/gtk.css
GTK4_DIR=~/.themes/$selected/gtk-4.0/gtk.css

sed -i "s/#1e1e2e/$background/g" $GTK3_DIR
sed -i "s/#89b4fa/$foreground/g" $GTK3_DIR
sed -i "s/#11111b/$background/g" $GTK3_DIR
sed -i "s/#313244/$background/g" $GTK3_DIR
sed -i "s/#FFFFFF/$foreground/g" $GTK3_DIR
sed -i "s/#bad3fc/$foreground/g" $GTK3_DIR
sed -i "s/#f38ba8/$foreground/g" $GTK3_DIR
sed -i "s/#40404d/$foreground/g" $GTK3_DIR
sed -i "1768s/.*/color: $background;/g" $GTK3_DIR

sed -i "s/#1e1e2e/$background/g" $GTK4_DIR
sed -i "s/#89b4fa/$foreground/g" $GTK4_DIR
sed -i "s/#11111b/$background/g" $GTK4_DIR
sed -i "s/#313244/$background/g" $GTK4_DIR
sed -i "s/#FFFFFF/$foreground/g" $GTK4_DIR
sed -i "s/#bad3fc/$foreground/g" $GTK4_DIR
sed -i "s/#f38ba8/$foreground/g" $GTK4_DIR

cp -R ~/.themes/$selected/gtk-4.0/* ~/.config/gtk-4.0
gsettings set org.gnome.desktop.interface gtk-theme $selected