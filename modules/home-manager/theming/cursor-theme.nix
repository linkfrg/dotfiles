{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.theming.cursorTheme;
in {
  options.linkfrg-dotfiles.theming.cursorTheme = {
    enable = lib.mkEnableOption "Enable cursor theme";
  };

  config = lib.mkIf cfg.enable {
    home.pointerCursor = {
      size = 24;
      gtk.enable = true;
      x11.enable = true;
      name = "Adwaita";
      package = pkgs.adwaita-icon-theme;
    };
  };
}
