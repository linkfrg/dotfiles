{
  config,
  lib,
  ...
}: let
  cfg = config.custom.services.xdgUserDirs;
in {
  options.custom.services.xdgUserDirs = {
    enable = lib.mkEnableOption "Enable XDG User Dirs";
  };

  config = lib.mkIf cfg.enable {
    xdg.userDirs = {
      enable = true;
      createDirectories = true;
    };
  };
}
