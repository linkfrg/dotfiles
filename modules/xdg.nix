{
  flake.homeModules.userDirs = {
    xdg.userDirs = {
      enable = true;
      createDirectories = true;
    };
    xdg.userDirs.setSessionVariables = true;
  };

  flake.homeModules.mimeApps = let
    webBrowser = "firefox.desktop";
    imageViewer = "org.gnome.eog.desktop";
    videoPlayer = "mpv.desktop";
    archiver = "org.gnome.FileRoller.desktop";
  in {
    xdg.mimeApps = {
      enable = true;
      defaultApplications = {
        # Browser
        "default-web-browser" = [webBrowser];
        "text/html" = [webBrowser];
        "x-scheme-handler/http" = [webBrowser];
        "x-scheme-handler/https" = [webBrowser];
        "x-scheme-handler/about" = [webBrowser];
        "x-scheme-handler/unknown" = [webBrowser];
        "application/pdf" = [webBrowser];

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

        "application/zip" = [archiver];
        "application/x-7z-compressed" = [archiver];
        "application/x-rar-compressed" = [archiver];
        "application/x-tar" = [archiver];
        "application/gzip" = [archiver];
      };
    };
  };
}
