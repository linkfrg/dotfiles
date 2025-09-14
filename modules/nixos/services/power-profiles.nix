{
  lib,
  config,
  ...
}: let
  cfg = config.custom.services.power-profiles;
in {
  options.custom.services.power-profiles = {
    enable = lib.mkEnableOption "Enable Power Profiles Daemon";
  };

  config = lib.mkIf cfg.enable {
    services.power-profiles-daemon.enable = true;
  };
}
