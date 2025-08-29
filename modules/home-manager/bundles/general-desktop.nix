{
  config,
  lib,
  ...
}: let
  cfg = config.custom.bundles.general-desktop;
in {
  options.custom.bundles.general-desktop = {
    enable = lib.mkEnableOption "Enable General Desktop HM bundle";
    username = lib.mkOption {
      type = lib.types.str;
      description = "The username";
    };
  };

  config = lib.mkIf cfg.enable {
    home = {
      username = cfg.username;
      homeDirectory = "/home/${cfg.username}";
    };

    nixpkgs.config.allowUnfree = true;

    programs.home-manager.enable = true;

    home.stateVersion = "25.05";

    linkfrg-dotfiles = {
      hyprland.enable = true;
      hyprlock.enable = true;
      ignis.enable = true;
      kitty.enable = true;

      cursorTheme.enable = true;
      fonts.enable = true;
      iconTheme.enable = true;
    };

    custom = {
      services = {
        easyeffects.enable = true;
        xdgPortal.enable = true;
        xdgUserDirs.enable = true;
      };

      software = {
        firefox = {
          enable = true;
        };
        zed.enable = true;
        chromium.enable = true;
        common.enable = true;
        gtk.enable = true;
      };

      terminal = {
        btop.enable = true;
        develop.enable = true;
        direnv.enable = true;
        fastfetch.enable = true;
        fish.enable = true;
        git.enable = true;
        starship.enable = true;
      };
    };

    gtk.gtk3.bookmarks = [
      "file:///data"
      "file:///data/ignis"
      "file:///data/dotfiles"
    ];

    wayland.windowManager.hyprland.settings = {
      exec-once = [
        "Telegram -startintray"
      ];

      input = {
        kb_layout = "us, ru";
      };
    };
  };
}
