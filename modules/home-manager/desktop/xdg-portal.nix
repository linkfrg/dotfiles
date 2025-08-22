{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.desktop.xdgPortal;
in {
  options.custom.desktop.xdgPortal = {
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
