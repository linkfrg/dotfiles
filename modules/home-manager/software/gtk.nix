{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.software.gtk;
in {
  options.linkfrg-dotfiles.software.gtk = {
    enable = lib.mkEnableOption "Enable Gtk";
  };

  config = lib.mkIf cfg.enable {
    dconf = {
      settings = {
        "org/gnome/desktop/interface" = {
          color-scheme = "prefer-dark";
        };
      };
    };

    gtk = {
      enable = true;

      gtk3.bookmarks = [
        "file:///${config.xdg.userDirs.documents}"
        "file:///${config.xdg.userDirs.pictures}"
        "file:///${config.xdg.userDirs.videos}"
        "file:///${config.xdg.userDirs.download}"
      ];
    };
  };
}
