{inputs, ...}: {
  flake.homeModules.firefox-nvidia = {
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
  };

  flake.homeModules.firefox = {
    pkgs,
    config,
    ...
  }: let
    firefox-addons = inputs.firefox-addons.packages.${pkgs.stdenv.hostPlatform.system};
  in {
    programs.firefox = {
      enable = true;
      configPath = "${config.xdg.configHome}/mozilla/firefox";

      # Check about:policies#documentation for options
      policies = {
        DisableTelemetry = true;
        DisableFirefoxStudies = true;
        EnableTrackingProtection = {
          Value = true;
          Locked = true;
          Cryptomining = true;
          Fingerprinting = true;
          EmailTracking = true;
        };
        DisableFirefoxAccounts = true;
        DisableAccounts = true;
        OverrideFirstRunPage = "";
        OverridePostUpdatePage = "";
        DontCheckDefaultBrowser = true;
        DisplayBookmarksToolbar = "always";
        OfferToSaveLogins = false;
        PasswordManagerEnabled = false;
      };

      profiles.default = {
        id = 0;
        name = "default";
        isDefault = true;

        extensions.packages = with firefox-addons; [
          ublock-origin
          darkreader
          bitwarden
          sponsorblock
          bonjourr-startpage
          translate-web-pages
        ];

        settings = {
          "extensions.autoDisableScopes" = 0; # enable all extensions by default
        };
      };
    };
  };
}
