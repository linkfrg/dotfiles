{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.xdgUserDirs;
in {
  options.linkfrg-dotfiles.services.xdgUserDirs = {
    enable = lib.mkEnableOption "Enable XDG User Dirs";
  };

  config = lib.mkIf cfg.enable {
    xdg.userDirs = {
      enable = true;
      createDirectories = true;
    };
  };
}
