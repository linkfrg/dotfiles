#!/bin/bash

hyprland_nvidia="
    hyprland-nvidia-git
    libva-nvidia-driver-git
    nvidia-dkms
"

hyprland_not_nvidia="
    hyprland-git
"

hyprland_base="
    xdg-desktop-portal-hyprland
    xorg-xwayland
    qt5-wayland
    qt6-wayland
    qt5ct
    qt6ct
    libva
    linux-headers 
"

pipewire_stage="
    pipewire 
    pipewire-alsa 
    pipewire-pulse 
    pipewire-jack 
    pavucontrol
    wireplumber
"

components="
    mako
    jq
    waybar
    rofi-lbonn-wayland
    cava
    polkit-gnome
    swww
    gtklock
    pamixer 
    cliphist
    python-pywal
    grimblast-git
    swayimg
    network-manager-applet 
    kitty
    thunar
    thunar-archive-plugin 
    file-roller 
    gtk-engine-murrine 
    gnome-themes-extra
    xdg-user-dirs
"

additional_programs="
    firefox 
    eog
    nwg-look
    sddm-git
    telegram-desktop
    obs-studio
"

font="
    ttf-jetbrains-mono
    ttf-nerd-fonts-symbols
    papirus-icon-theme
"

read -rep $'Do you want to proceed with installation? (y, n) ' ANSWER

if [[ $ANSWER == "Y" || $ANSWER == "y" ]]; then
    read -rep $'Do you have nvidia gpu (y, n) ' ANSWER
    if [[ $ANSWER == "Y" || $ANSWER == "y" ]]; then
        NVIDIA=true
    elif [[ $ANSWER == "N" || $ANSWER == "n" ]]; then
        NVIDIA=false
    else
        echo "Error! type 'y' or 'n' Exit..."
    fi
else
    echo "Exit..."
    exit 0
fi


# PARU
read -rep $'Install paru? (y, n) ' ANSWER
if [[ $ANSWER == "Y" || $ANSWER == "y" ]]; then
    sudo pacman -S --needed base-devel
    git clone https://aur.archlinux.org/paru.git
    cd paru
    makepkg -si
    rm -R ./paru
elif [[ $ANSWER == "N" || $ANSWER == "n" ]]; then
    echo "Skipping paru install..."
else
    echo "Error! type 'y' or 'n' Exit..."
fi

# INSTALLING REQUIRED PACKAGES
if [ $NVIDIA == true ]; then
    echo "Installing hyprland for nvidia..."
    paru -S --needed $hyprland_nvidia $pipewire_stage $hyprland_base $components $font
    xdg-user-dirs-update
    systemctl --user enable --now pipewire.service pipewire.socket pipewire-pulse.service wireplumber.service
else
    echo "Installing hyprland for not nvidia..."
    paru -S --needed $hyprland_not_nvidia $pipewire_stage $hyprland_base $components $font
    xdg-user-dirs-update
    systemctl --user enable --now pipewire.service pipewire.socket pipewire-pulse.service wireplumber.service
fi

# COPYING CONFIG FILES
read -rep $'Copy config files? (y, n) ' ANSWER
if [[ $ANSWER == "Y" || $ANSWER == "y" ]]; then
    echo "Coping config files..."
    cp -R home/.config/* ~/.config/
    cp -R home/.themes ~/
    cp -R home/.wallpaper ~/
elif [[ $ANSWER == "N" || $ANSWER == "n" ]]; then
    echo "Skipping config files copy..."
else
    echo "Error! type 'y' or 'n' Exit..."
fi

# SDDM
read -rep $'Install sddm? (y, n) ' ANSWER
if [[ $ANSWER == "Y" || $ANSWER == "y" ]]; then
    paru -S --needed sddm
elif [[ $ANSWER == "N" || $ANSWER == "n" ]]; then
    echo "Skipping sddm install..."
else
    echo "Error! type 'y' or 'n' Exit..."
fi

# ADDITIONAL PROGRAMS
read -rep $'Install additional programs(firefox, eye of gnome, nwg-look, telegram, obs-studio)? (y, n) ' ANSWER
if [[ $ANSWER == "Y" || $ANSWER == "y" ]]; then
    paru -S --needed $additional_programs
elif [[ $ANSWER == "N" || $ANSWER == "n" ]]; then
    echo "Skipping additional programs installation..."
else
    echo "Error! type 'y' or 'n' Exit..."
fi

# PYWAL COLORSCHEME
wal -i ~/.wallpaper/wallpaper3.png -n -t

# SETTING UP THEME, FONT, ICONS

gsettings set org.gnome.desktop.interface gtk-theme Monet
gsettings set org.gnome.desktop.interface icon-theme Papirus
gsettings set org.gnome.desktop.interface font-name "JetBrains Mono Regular 11"

mkdir ~/.config/mako
mkdir ~/.config/swayimg
ln -sf ~/.cache/wal/colors-mako ~/.config/mako/config
ln -sf ~/.cache/wal/swayimg ~/.config/swayimg/config
