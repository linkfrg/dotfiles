{pkgs, ...}: let
  imageViewer = "org.gnome.eog.desktop";
  videoPlayer = "mpv.desktop";
  browser = "firefox";
  archiver = "org.gnome.FileRoller";
in {
  home.packages = with pkgs; [
    telegram-desktop
    ayugram-desktop
    vesktop
    protonvpn-gui
    eog
    transmission_4-gtk
    xorg.xeyes
    uxplay
    pinta
    gnome-calculator
    linux-wifi-hotspot
    snapshot
    pavucontrol
    obsidian
  ];

  programs.onlyoffice.enable = true;
  programs.chromium.enable = true;

  programs.mpv = {
    enable = true;
    config = {
      audio-file-auto = "fuzzy";
    };
  };

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

      "text/html" = [browser];
      "application/pdf" = [browser];
      "application/zip" = [archiver];
      "application/x-7z-compressed" = [archiver];
      "application/x-rar-compressed" = [archiver];
      "application/x-tar" = [archiver];
      "application/gzip" = [archiver];
    };
  };
}
