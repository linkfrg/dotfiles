{
  config,
  lib,
  ...
}: let
  cfg = config.custom.services.upower;
in {
  options.custom.services.upower = {
    enable = lib.mkEnableOption "Enable UPower";
  };

  config = lib.mkIf cfg.enable {
    services.upower.enable = true;
  };
}
