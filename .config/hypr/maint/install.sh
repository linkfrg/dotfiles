#!/bin/bash

export FZF_HEIGHT="40%"
MAINTENANCE_DIR=".config/hypr/maint"
CONF_DIR="dotfiles"

# specify the repo branch
if [ -z "$1" ]; then
    BRANCH="master"
else
    BRANCH=$1
fi

if [ -d "$CONF_DIR" ]; then
    echo "$CONF_DIR directory exists."
else
    echo "$CONF_DIR directory does not exist. Cloning the repository..."
    git clone https://github.com/linkfrg/dotfiles.git --depth 1 --branch main
fi

# Change branch to the specified branch
cd $CONF_DIR
git checkout $BRANCH
git fetch origin $BRANCH
git reset --hard origin/$BRANCH

source $MAINTENANCE_DIR/essentials.sh # source the essentials file INSIDE the repository

install_git

install_fzf

install_figlet

# choose Pacman Wrapper
echo "Choose an AUR helper to install packages:"
aur_helpers=("yay" "paru")
aur_helper=$(echo "${aur_helpers[@]}" | tr ' ' '\n' | fzf --height $FZF_HEIGHT)
echo "AUR helper selected: $aur_helper"
case $aur_helper in
yay)
    install_yay
    ;;
paru)
    install_paru
    ;;
esac

continue_prompt "Backing up dotfiles from .config ..." "$MAINTENANCE_DIR/backup.sh"

continue_prompt "Copying configuration files to $HOME..." "cd dotfiles \ mkdir -p ~/.local/share/themes \ cp -R .config/* ~/.config/ \ cp -R ignis ~/.config/ \ cp -R Material ~/.local/share/themes"

continue_prompt "Do you want to install necessary packages? (using $aur_helper)" "$HOME/.config/hypr/maint/pkgs.sh $aur_helper"

continue_prompt "Do you want to install NVidia compatability? (using $aur_helper)" "$HOME/.config/hypr/maint/pkgs-nvidia.sh $aur_helper"

echo "Installation complete. Please Reboot the system."
