{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.theming.iconTheme;
in {
  options.linkfrg-dotfiles.theming.iconTheme = {
    enable = lib.mkEnableOption "Enable icon theme";
  };

  config = lib.mkIf cfg.enable {
    gtk.iconTheme = {
      name = "Papirus";
      package = pkgs.papirus-icon-theme;
    };
  };
}
