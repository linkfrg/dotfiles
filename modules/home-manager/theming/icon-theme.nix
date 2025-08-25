{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.theming.iconTheme;
in {
  options.custom.theming.iconTheme = {
    enable = lib.mkEnableOption "Enable icon theme";
  };

  config = lib.mkIf cfg.enable {
    gtk.iconTheme = {
      name = "Papirus";
      package = pkgs.papirus-icon-theme;
    };
  };
}
