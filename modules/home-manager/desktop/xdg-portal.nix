{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.desktop.xdgPortal;
in {
  options.linkfrg-dotfiles.desktop.xdgPortal = {
    enable = lib.mkEnableOption "Enable XDG Desktop Portal";
  };

  config = lib.mkIf cfg.enable {
    xdg.portal = {
      enable = true;
      extraPortals = [pkgs.xdg-desktop-portal-gtk];
      xdgOpenUsePortal = true;
    };
  };
}
