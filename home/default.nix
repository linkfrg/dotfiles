{inputs, ...}: {
  imports = [
    ./desktop/niri
    ./desktop/hyprlock
    ./desktop/ignis.nix
    ./desktop/fonts.nix
    ./desktop/pointer-cursor.nix
    ./games.nix
    ./terminal
    ./software
    ./services
    inputs.dotfiles-private.homeManagerModules.default
  ];

  home = {
    username = "link";
    homeDirectory = "/home/link";
  };

  home.stateVersion = "25.05";
}
