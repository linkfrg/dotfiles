{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.software.kitty;
in {
  options.linkfrg-dotfiles.software.kitty = {
    enable = lib.mkEnableOption "Enable kitty";
  };

  config = lib.mkIf cfg.enable {
    programs.kitty = {
      enable = true;
      settings = {
        include = "~/.cache/ignis/material/dark_colors-kitty.conf";
        font_size = 12;
        font_family = "JetBrainsMono";
        window_margin_width = 15;
        remember_window_size = "no";
        background_opacity = 1;
      };
    };
  };
}
