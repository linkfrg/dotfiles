{
  flake.homeModules.tmux = {
    pkgs,
    config,
    ...
  }: {
    xdg.configFile."tmux".source =
      config.lib.file.mkOutOfStoreSymlink "${config.home.homeDirectory}/Projects/dotfiles/config/tmux";

    home.packages = with pkgs; [
      tmux
    ];
  };
}
