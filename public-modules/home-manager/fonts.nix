{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.fonts;
in {
  options.linkfrg-dotfiles.fonts = {
    enable = lib.mkEnableOption "Enable JetBrains fonts";
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
