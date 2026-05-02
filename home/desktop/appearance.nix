{pkgs, config, ...}: {
  fonts.fontconfig.enable = true;

  home.packages = with pkgs; [
    jetbrains-mono
    nerd-fonts.jetbrains-mono
  ];

  gtk.font.name = "JetBrains Mono";

  home.pointerCursor = {
    size = 24;
    gtk.enable = true;
    x11.enable = true;
    name = "Adwaita";
    package = pkgs.adwaita-icon-theme;
  };

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
    gtk4.theme = config.gtk.theme;
    gtk3.bookmarks = [
      "file:///${config.xdg.userDirs.documents}"
      "file:///${config.xdg.userDirs.pictures}"
      "file:///${config.xdg.userDirs.videos}"
      "file:///${config.xdg.userDirs.download}"
    ];
  };

}
