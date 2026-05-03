{ inputs, config, ... }:
let
  base_path = "${config.home.homeDirectory}/Projects/dotfiles";
  ln = path: config.lib.file.mkOutOfStoreSymlink "${base_path}/home/${path}";
in
{
  imports = [
    inputs.ignis.homeManagerModules.default
    ./desktop/niri
    ./desktop/hyprlock
    ./desktop/ignis.nix
    ./desktop/appearance.nix
    ./services/xdg.nix
    ./services/wlsunset.nix
    ./terminal
    ./software
    ./games.nix
  ];

  xdg.configFile."tmux".source = ln "tmux";

  home = {
    username = "link";
    homeDirectory = "/home/link";
  };

  home.stateVersion = "25.05";
}
