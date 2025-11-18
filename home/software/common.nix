{pkgs, ...}: let
  imageViewer = "org.gnome.eog.desktop";
  videoPlayer = "mpv.desktop";
in {
  home.packages = with pkgs; [
    telegram-desktop
    ayugram-desktop
    vesktop
    protonvpn-gui
    eog
    mpv
    transmission_4-gtk
    xorg.xeyes
    uxplay
    pinta
    gnome-calculator
    linux-wifi-hotspot
    snapshot
    pavucontrol
  ];

  programs.onlyoffice.enable = true;
  programs.chromium.enable = true;
  programs.obsidian.enable = true;

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
}
