{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.hyprland;
in {
  options.linkfrg-dotfiles.hyprland = {
    enable = lib.mkEnableOption "Enable Hyprland";
  };

  config = lib.mkIf cfg.enable {
    home.packages = with pkgs; [
      grimblast
      wl-clipboard
      polkit_gnome
    ];

    wayland.windowManager.hyprland = {
      enable = true;
      settings = lib.mkMerge [
        (import ./exec.nix)
        (import ./general.nix)
        (import ./keybinds.nix)
        (import ./rules.nix)
        (import ./monitors.nix)
        (import ./env.nix)
      ];
      extraConfig = import ./colors.nix;
    };
  };
}
