{pkgs, config, ...}: {
    home.packages = [
        pkgs.tmux
    ];

    home.file.".tmux.conf".source = config.lib.file.mkOutOfStoreSymlink "/data/dotfiles/home/terminal/tmux/tmux.conf"; 
}
