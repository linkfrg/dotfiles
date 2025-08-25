{
  config,
  lib,
  ...
}: let
  cfg = config.custom.terminal.fish;
in {
  options.custom.terminal.fish = {
    enable = lib.mkEnableOption "Enable fish";
  };

  config = lib.mkIf cfg.enable {
    programs.fish = {
      enable = true;
      interactiveShellInit = ''
        set -g fish_greeting
        set --global fish_color_command blue
      '';
    };

    documentation.man.generateCaches = false; # speed up building
  };
}
