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
    ripgrep
    playerctl
    gradience-git
    adw-gtk3-git
    jq
    eww-tray-wayland-git
    polkit-gnome
    swww
    gtklock
    pamixer 
    cliphist
    grimblast-git
    gnome-control-center
    kitty
    thunar
    thunar-archive-plugin 
    file-roller 
    xdg-user-dirs
    wf-recorder
    dbus-python
    python-gobject
    python-requests
    python-jinja
    python-material-color-utilities
    zenity
    socat
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
    cp -R .config/* ~/.config/
    cp -R .wallpaper ~/
elif [[ $ANSWER == "N" || $ANSWER == "n" ]]; then
    echo "Skipping config files copy..."
else
    echo "Error! type 'y' or 'n' Exit..."
fi

# SETTING UP THEME, FONT, ICONS

gsettings set org.gnome.desktop.interface gtk-theme adw-gtk3
gsettings set org.gnome.desktop.interface icon-theme Papirus
gsettings set org.gnome.desktop.interface font-name "JetBrains Mono Regular 11"
