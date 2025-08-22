{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.theming.fonts;
in {
  options.custom.theming.fonts = {
    enable = lib.mkEnableOption "Enable fonts";
  };

  config = lib.mkIf cfg.enable {
    fonts.fontconfig.enable = true;

    home.packages = with pkgs; [
      jetbrains-mono
      nerd-fonts.jetbrains-mono
    ];

    gtk.font.name = "JetBrains Mono";
  };
}
