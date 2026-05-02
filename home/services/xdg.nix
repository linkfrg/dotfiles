let
  imageViewer = "org.gnome.eog.desktop";
  videoPlayer = "mpv.desktop";
  archiver = "org.gnome.FileRoller.desktop";
in
{
  xdg.userDirs = {
    enable = true;
    createDirectories = true;
  };
  xdg.userDirs.setSessionVariables = true;

  xdg.mimeApps = {
    enable = true;
    defaultApplications = {
      # Images
      "image/jpeg" = [ imageViewer ];
      "image/png" = [ imageViewer ];
      "image/gif" = [ imageViewer ];
      "image/webp" = [ imageViewer ];
      "image/tiff" = [ imageViewer ];
      "image/bmp" = [ imageViewer ];

      # Videos
      "video/mp4" = [ videoPlayer ];
      "video/x-matroska" = [ videoPlayer ]; # mkv
      "video/webm" = [ videoPlayer ];
      "video/x-msvideo" = [ videoPlayer ]; # avi
      "video/quicktime" = [ videoPlayer ]; # mov

      "application/zip" = [ archiver ];
      "application/x-7z-compressed" = [ archiver ];
      "application/x-rar-compressed" = [ archiver ];
      "application/x-tar" = [ archiver ];
      "application/gzip" = [ archiver ];
    };
  };

}
