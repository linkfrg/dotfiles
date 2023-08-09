#!/bin/bash

hyprland_nvidia="
    hyprland-nvidia-git
    xdg-desktop-portal-hyprland
    xorg-xwayland
    qt5-wayland
    qt6-wayland
    qt5ct
    qt6ct
    libva
    libva-nvidia-driver-git
    linux-headers 
    nvidia-dkms
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
    grim
    slurp
    wl-clipboard
"

soft="
    network-manager-applet 
    kitty
    thunar
    cmatrix
    neofetch
    hyprpicker-git
    firefox 
    eog
    thunar-archive-plugin 
    file-roller 
    nwg-look
    zsh
    sddm-git
"

misc="
    gtk-engine-murrine 
    gnome-themes-extra
    xdg-user-dirs
    ntfs-3g
"

font="
    ttf-jetbrains-mono
    ttf-nerd-fonts-symbols
    papirus-icon-theme
"




# PARU
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
rm -R ./paru

# INSTALL
paru -S $hyprland_nvidia $pipewire_stage $components $soft $misc $font


# USER DIRS
xdg-user-dirs-update

# PIPEWIRE
systemctl --user enable --now pipewire.service pipewire.socket pipewire-pulse.service wireplumber.service

# ZSH
chsh -s /usr/bin/zsh

# COPY CONFIG FILES
cp -R .config/* ~/.config/
cp -R .wallpaper ~/
cp -R .p10k.zsh ~/
cp -R .zshrc ~/
cp -R .oh-my-zsh ~/
mkdir ~/.local/share/applications/
cp .local/share/applications/code.desktop ~/.local/share/applications/

# PYWAL COLORSCHEME
wal -i ~/.wallpaper/wallpaper5.png -n -t
