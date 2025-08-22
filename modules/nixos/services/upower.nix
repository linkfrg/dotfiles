{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.upower;
in {
  options.linkfrg-dotfiles.services.upower = {
    enable = lib.mkEnableOption "Enable UPower";
  };

  config = lib.mkIf cfg.enable {
    services.upower.enable = true;
  };
}
