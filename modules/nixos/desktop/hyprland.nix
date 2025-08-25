{
  config,
  lib,
  ...
}: let
  cfg = config.custom.desktop.hyprland;
in {
  options.custom.desktop.hyprland = {
    enable = lib.mkEnableOption "Enable Hyprland";
  };

  config = lib.mkIf cfg.enable {
    programs.hyprland.enable = true;
  };
}
