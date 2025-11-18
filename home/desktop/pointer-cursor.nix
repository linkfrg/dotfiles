{pkgs, ...}: {
  home.pointerCursor = {
    size = 24;
    gtk.enable = true;
    x11.enable = true;
    name = "Adwaita";
    package = pkgs.adwaita-icon-theme;
  };
}
