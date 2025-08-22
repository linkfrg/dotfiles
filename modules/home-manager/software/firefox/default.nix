{
  inputs,
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.software.firefox;
  firefox-addons = inputs.firefox-addons.packages.${pkgs.system};
in {
  options.linkfrg-dotfiles.software.firefox = {
    enable = lib.mkEnableOption "Enable Firefox";
    nvidia = lib.mkEnableOption "Enable Nvidia spefic settings";
  };

  config = lib.mkIf cfg.enable (
    lib.mkMerge [
      {
        programs.firefox = {
          enable = true;

          # Check about:policies#documentation for options
          policies = import ./policies.nix;

          profiles.default = {
            id = 0;
            name = "default";
            isDefault = true;

            extensions.packages = import ./extensions.nix {inherit firefox-addons;};
            settings = import ./settings.nix;
            bookmarks = import ./bookmarks.nix;
          };
        };
      }
      (lib.mkIf cfg.nvidia {
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
      })
    ]
  );
}
