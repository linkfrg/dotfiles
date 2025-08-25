{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.software.common;
in {
  options.custom.software.common = {
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

    xdg.mimeApps = {
      enable = true;
      defaultApplications = {
        # Images
        "image/jpeg" = ["eog.desktop"];
        "image/png" = ["eog.desktop"];
        "image/gif" = ["eog.desktop"];
        "image/webp" = ["eog.desktop"];
        "image/tiff" = ["eog.desktop"];
        "image/bmp" = ["eog.desktop"];

        # Videos
        "video/mp4" = ["mpv.desktop"];
        "video/x-matroska" = ["mpv.desktop"]; # mkv
        "video/webm" = ["mpv.desktop"];
        "video/x-msvideo" = ["mpv.desktop"]; # avi
        "video/quicktime" = ["mpv.desktop"]; # mov
      };
    };
  };
}
