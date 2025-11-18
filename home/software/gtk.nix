{
  config,
  pkgs,
  ...
}: {
  dconf = {
    settings = {
      "org/gnome/desktop/interface" = {
        color-scheme = "prefer-dark";
      };
    };
  };

  gtk = {
    enable = true;

    iconTheme = {
      name = "Papirus";
      package = pkgs.papirus-icon-theme;
    };

    gtk3.bookmarks = [
      "file:///${config.xdg.userDirs.documents}"
      "file:///${config.xdg.userDirs.pictures}"
      "file:///${config.xdg.userDirs.videos}"
      "file:///${config.xdg.userDirs.download}"
      "file:///data"
      "file:///data/ignis"
      "file:///data/dotfiles"
    ];
  };
}
