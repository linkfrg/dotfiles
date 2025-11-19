{inputs, ...}: {
  imports = [
    inputs.ignis.homeManagerModules.default
    inputs.dotfiles-private.homeManagerModules.default
    ./desktop/niri
    ./desktop/hyprlock
    ./desktop/ignis.nix
    ./desktop/fonts.nix
    ./desktop/pointer-cursor.nix
    ./games.nix
    ./terminal
    ./software
    ./services
  ];

  home = {
    username = "link";
    homeDirectory = "/home/link";
  };

  home.stateVersion = "25.05";
}
