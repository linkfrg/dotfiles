{
  inputs,
  pkgs,
  lib,
  config,
  ...
}: let
  cfg = config.custom.desktop.niri;
in {
  imports = [
    inputs.niri-flake.homeModules.niri
  ];

  options.custom.desktop.niri = {
    enable = lib.mkEnableOption "Enable niri";
  };

  config = lib.mkIf cfg.enable {
    home.packages = with pkgs; [
      xwayland-satellite
      sway-contrib.grimshot
      nautilus # make open dialog work
    ];

    xdg.portal.extraPortals = with pkgs; [
      xdg-desktop-portal-gnome
    ];

    services.polkit-gnome.enable = true;

    programs.niri = {
      enable = true;
      package = pkgs.niri;
      settings = lib.mkMerge [
        (import ./binds.nix {inherit config;})
        ./input.nix
        ./layout.nix
        ./misc.nix
        ./outputs.nix
        ./rules.nix
        ./spawn.nix
      ];
    };
  };
}
