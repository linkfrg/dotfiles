{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.desktop.hyprland;
in {
  options.linkfrg-dotfiles.desktop.hyprland = {
    enable = lib.mkEnableOption "Enable Hyprland";
  };

  config = lib.mkIf cfg.enable {
    programs.hyprland.enable = true;
  };
}
