{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.software.common;
in let
  imageViewer = "org.gnome.eog.desktop";
  videoPlayer = "mpv.desktop";
in {
  options.custom.software.common = {
    enable = lib.mkEnableOption "Enable common software";
  };

  config = lib.mkIf cfg.enable {
    home.packages = with pkgs; [
      telegram-desktop
      protonvpn-gui
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
        "image/jpeg" = [imageViewer];
        "image/png" = [imageViewer];
        "image/gif" = [imageViewer];
        "image/webp" = [imageViewer];
        "image/tiff" = [imageViewer];
        "image/bmp" = [imageViewer];

        # Videos
        "video/mp4" = [videoPlayer];
        "video/x-matroska" = [videoPlayer]; # mkv
        "video/webm" = [videoPlayer];
        "video/x-msvideo" = [videoPlayer]; # avi
        "video/quicktime" = [videoPlayer]; # mov
      };
    };
  };
}
