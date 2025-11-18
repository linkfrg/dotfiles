{
  pkgs,
  lib,
  config,
  ...
}: {
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
    # enable = true;
    # package = pkgs.niri;
    settings = lib.mkMerge [
      (import ./binds.nix {inherit config;})
      ./input.nix
      ./layout.nix
      ./misc.nix
      ./rules.nix
      ./spawn.nix
    ];
  };
}
