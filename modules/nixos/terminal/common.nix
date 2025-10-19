{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.terminal.common;
in {
  options.custom.terminal.common = {
    enable = lib.mkEnableOption "Enable common utils";
  };

  config = lib.mkIf cfg.enable {
    environment.systemPackages = with pkgs; [
      usbutils
      libva-utils
      tree
      file
      f2fs-tools
      gnome-disk-utility
    ];
  };
}
