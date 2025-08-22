{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.software.common;
in {
  options.linkfrg-dotfiles.software.common = {
    enable = lib.mkEnableOption "Enable common software";
  };

  config = lib.mkIf cfg.enable {
    home.packages = with pkgs; [
      telegram-desktop
      protonvpn-gui
      xfce.thunar
      xfce.thunar-archive-plugin
      file-roller
      eog
      mpv
      transmission_4-gtk
      xorg.xeyes
      uxplay
    ];
  };
}
