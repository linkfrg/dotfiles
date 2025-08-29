{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.programs.thunar;
in {
  options.custom.programs.thunar = {
    enable = lib.mkEnableOption "Enable Thunar file manager";
  };

  config = lib.mkIf cfg.enable {
    programs.thunar = {
      enable = true;
      plugins = with pkgs.xfce; [
        thunar-archive-plugin
      ];
    };

    programs.file-roller.enable = true;
    services.gvfs.enable = true;
    services.tumbler.enable = true;
  };
}
