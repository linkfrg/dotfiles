{
  # Enables hardware acceleration using nvidia-vaapi-driver
  # See https://github.com/elFarto/nvidia-vaapi-driver?tab=readme-ov-file#firefox
  programs.firefox.profiles.default.settings = {
    "media.ffmpeg.vaapi.enabled" = true;
    "media.hardware-video-decoding.force-enabled" = true;
    "media.rdd-ffmpeg.enabled" = true;
    "media.av1.enabled" = false;
    "widget.dmabuf.force-enabled" = true;
  };

  home.sessionVariables = {
    MOZ_DISABLE_RDD_SANDBOX = "1";
  };
}
