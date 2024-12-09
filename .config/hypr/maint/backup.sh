#!/bin/bash

figlet "Backup"

backup_dotfiles() {
    local date=$(date +%Y%m%d)
    local backup_dir="$HOME/dotfiles_backup_$date"
    mkdir -p "$backup_dir"

    cp -r $HOME/.config "$backup_dir"

    echo "Dotfiles have been copied to $backup_dir."
}

restore_dotfiles() {
    local backup_dir=$(ls -d dotfiles_backup_* | tail -n 1)

    if [ -z "$backup_dir" ]; then
        echo "No backup directory found."
        exit 1
    fi

    # Restore backup using rsync
    rsync -av --ignore-existing "$HOME/$backup_dir/" ~/

    if [ -z "$(ls -A "$backup_dir")" ]; then
        rmdir "$backup_dir"
    else
        echo "$backup_dir is not empty, not removing."
    fi

    echo "Dotfiles have been restored."
}

# check if argument is --restore
if [ "$1" == "--restore" ]; then
    restore_dotfiles
else
    backup_dotfiles
fi
